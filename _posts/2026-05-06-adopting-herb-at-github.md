---
layout: post
title: "Adopting Herb at GitHub"
description: "We've spent the past few months integrating Herb into the GitHub.com monolith. It caught numerous bugs, allowed us to migrate off the effectively-archived erb_lint, and X. In this talk, I'll share how you can see similar benefts in your codebase today and help improve the project ahead of its 1.0 release."
image: TODO
---

_A transcript of my spring 2026 lightning talk, as presented at Boulder Ruby._

_Bio: Joel is a staff software engineer at GitHub, working on the health of the GitHub.com Rails monolith._

_Abstract: We've spent the past few months integrating Herb into the GitHub.com monolith. It caught numerous bugs, allowed us to migrate off the effectively-archived erb_lint, and X. In this talk, I'll share how you can see similar benefts in your codebase today and help improve the project ahead of its 1.0 release._

Before I get started, how many people here have heard of Herb?

For those that haven't, Herb is `An ecosystem of powerful and seamless developer tools for HTML+ERB (HTML + Embedded Ruby) templates.`, created by Marco Roth. The crown jewel of the Herb ecosystem is the Herb parser, which is written in C. Based on Prism, its syntax tree is the basis for all the modern developer experience features you'd expect but were otherwise missing from the ERB stack, like a language server, formatter, etc.

Marco has been on a world-wide speaking tour presenting his work on the project. Last I checked, he had [seven talks on Ruby Events](https://www.rubyevents.org/profiles/marcoroth) already this year! I'd encourage you to check them out to learn more about the project.

Today, I'm going to share our experience adopting Herb at GitHub and why you should do the same in your codebase. I'll also share a few things you'll wish you never knew about ERB.

## Why we are adopting Herb

Herb may replace Erubi in the next major Rails release, as a backwards-compatible replacement. As GitHub is almost certainly the most prolific renderer of ERB in the world, Marco asked us to help validate Herb before it lands in Rails.

How prolific? We have around about a half million lines of ERB across about 10,000 files, so about 50 lines/file on average. Despite building most of our new UI in React, we still added 350 files with over 15,000 lines of ERB in the past year, twice as much as we did in the year prior.

While the Herb test suite is quite thorough, there was no substitute for testing it against a real, large-scale codebase. So that's what we've been doing since December.

## Our process

When we started out, Herb could not parse all of our ERB, in part due to errors in our ERB and shortcomings in the Herb parser. Those two categories of issues would prove to be the ongoing framing for the work, with our goal of meeting in the middle, where our errors were resolved and Herb could parse every `.html.erb` in our codebase.

Our test was simple. We aimed to pass `npx @herb-tools/linter` with only the `parser-no-errors` rule enabled. The first time we ran the linter, less than 75% of our ERB files passed. We had 2,768 files to fix! Thankfully, the bugs Herb caught in our codebase were mostly benign.

## Bugs found by Herb

### Invalid HTML

It found piles of missing closing tags. As it turns out, browsers are pretty tolerant of bad HTML and will effectively close unclosed tags for you:

```html+erb
<p>Hello World! <%# missing </p> %>
```

```html+erb
</div
```


There were also similarly many cases where the closing tags for elements or ERB blocks were swapped:

```html+erb
<% if active? %>
<span>Hello World!
<% end %>
</span>
```

### Conditional opening/closing tags

In other cases, we did things in ERB that are difficult to translate into an AST, such as conditional opening and closing tags:

```html+erb
<% if show_wrapper? %>
  <div class="wrapper">
<% end %>
  <p>Content</p>
<% if show_wrapper? %>
  </div>
<% end %>
```

Which we fixed by switching to:

```html+erb
<% content = capture do %>
  <p>Content</p>
<% end %>

<% if show_wrapper? %>
  <div class="wrapper"><%= content %></div>
<% else %>
  <%= content %>
<% end %>
```

We had about 150 cases like this, which you might think would have been pretty painful to refactor. And you would have been right a year ago! But with the recent Claude Opus models, we've had a basically 100% success rate of one-shot fixes simply by pasting in the Herb error. Herb does of course have a `--fix` option as well, but for the cases where it doesn't, AI has done a very effective job.

Herb has since added support for this pattern in https://github.com/marcoroth/herb/pull/1153, but I think this is a case where the refactored code is just better anyways.

### Invalid ruby

But some of the bugs were quite serious. We caught invalid Ruby in quite a few places:

```html+erb
<% if x.y? && x.z? && %>
```

```html+erb
<% if x? do %>
```

### Validating fixes

Manual validation, Blind renderer, etc

## Bugs found in Herb

ERB is the worst version of Hyrum's law. Our test suite revealed a couple bugs in Herb.

### Whitespace bugs

For example, the following template:

```html+erb
hello<%= -%>
world
```

Would output `helloworld` in Erubi, but in Herb would output:

```
hello
world
```

Link: https://github.com/marcoroth/herb/pull/1361

There were a few other similar whitespace edge cases. https://github.com/marcoroth/herb/pull/1366 https://github.com/marcoroth/herb/pull/1553 https://github.com/marcoroth/herb/pull/1554

### Invalid Ruby

In another case, when a comment is on the same line as an `end` produced invalid ruby.

```html+erb
<%= render Foo.new do %>
  hello
<% end # comment %>
```

https://github.com/marcoroth/herb/pull/1363

TODO explain why this is super bad and rails should handle it
Still have to verify to be confident shipping

### Vendored templates

Herb, unlike Erubi, can throw runtime exceptions when encountering ERB it couldn't parse, including ERB from vendored gems not under GitHub's control. If a gem shipped invalid ERB (by Herb's standards), it could crash production at request time.

This was particularly dangerous because GitHub vendors hundreds of gems, many containing ERB templates. Gem authors wouldn't know their ERB was "invalid" under the new parser. The failure mode is a 500 error, not a graceful degradation. 

The mitigation was a CI check that force-compiles all vendored `.erb` files at build time, catching incompatibilities before they reach production. 

TODO PRs to upstream, graphql-ruby https://github.com/rmosolgo/graphql-ruby/pull/5497, primer viewcomponents https://github.com/primer/view_components/pull/3850

### Performance impact

Cold render impact, we already use actionview precompiler

Precompiler slow down
ViewComponent slow down
Cold render problem, issues outstanding

A LUC (Live User Canary) test confirmed that while Herb had no impact on request latency (validating the hypothesis), it increased ViewPrecompiler.precompile time from ~15s to ~60s in production — an unacceptable addition to deploy times.

In a Codespace benchmark:

Erubi: 11.8s average
Herb: 22.6s average (+91%)
This single finding blocked production deployment for weeks and triggered a multi-pronged engineering effort:

An ActionView::Precompiler cache (abandoned — too hacky)
A Herb-level build cache (invalid due to ReActionView config changes)
A ReActionView-level build cache (successful: 13.2s, on par with Erubi)
The team ultimately decided to wait to ship to production until the caching solution was accepted upstream, rather than deploying a fork.

### Even GitHub doesn't use all of Erubi

The Erubi test suite has 108 tests. Github passed CI with herb on, but 8 erubi tests failed (https://github.com/marcoroth/herb/pull/1548). Even at our scale, we do not use all of the features of Erubi. 

## Wrapping up

Give Herb a try! I have no hesitation recommending turning it on for dev and test, where you'll see most of the benefits over Erubi anyways.