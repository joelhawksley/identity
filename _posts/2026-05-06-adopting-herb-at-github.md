---
layout: post
title: "Adopting Herb at GitHub"
description: "We've spent the past few months integrating Herb into the GitHub.com monolith. It caught numerous bugs missed by our existing tooling, allowed us to migrate off the effectively-archived erb_lint, and X. In this talk, I'll share how you can see similar benefts in your codebase today and help improve the project ahead of its 1.0 release."
image: TODO
---

_A transcript of a spring 2026 lightning talk, as presented at Boulder Ruby._

_Bio: Joel is a staff software engineer at GitHub, working on the health of the GitHub.com Rails monolith._

_Abstract: I've spent the past few months integrating Herb into the GitHub.com monolith. It caught numerous bugs, allowed us to migrate off the effectively-archived erb_lint, and X. In this talk, I'll share how you can see similar benefts in your codebase today and help improve the project ahead of its 1.0 release._

Before I get started, how many people here have heard of Herb?

For those that haven't, Herb is `An ecosystem of powerful and seamless developer tools for HTML+ERB (HTML + Embedded Ruby) templates.`, created by Marco Roth. The crown jewel of the Herb ecosystem is the Herb parser, which is written in C. Based on Prism, its syntax tree is the basis for all the modern developer experience features you'd expect but were otherwise missing from the ERB stack, like a language server, formatter, etc.

Marco has been on a world-wide speaking tour presenting his work on the project. Last I checked, he had [seven talks on Ruby Events](https://www.rubyevents.org/profiles/marcoroth) already this year! I'd encourage you to check them out to learn more about the project.

Today, I'm going to share our experience adopting Herb at GitHub and why I think you should do the same in your codebase. I'll also share a few things you'll wish you never knew about ERB.

## Why we are adopting Herb

The Rails core is interested in having Herb replace Erubi. As GitHub is almost certainly the most prolific renderer of ERB in the world, Marco asked us to help validate Herb before it lands in Rails.

How prolific? We have around about a half million lines of ERB across about 10,000 files, so about 50 lines/file on average. Despite building most of our new UI in React, we still added 350 files with over 15,000 lines of ERB in 2025, twice as much as we did in 2024.

While the Herb test suite is quite thorough, there was no substitute for testing it against a real, large-scale codebase. So that's what I've been doing since December.

## Our process

When I started out, Herb could not parse all of our ERB, due to both errors in our ERB and shortcomings in the Herb parser.

The first milestone was simple. I aimed to pass `npx @herb-tools/linter` with only the `parser-no-errors` rule enabled. The first time I ran the linter, less than 75% of our ERB files passed. I had 2,768 files to fix! Thankfully, the bugs Herb caught in our codebase were mostly benign.

## Bugs found by Herb

### Invalid HTML

Herb found piles of missing closing tags. As it turns out, browsers are pretty tolerant of bad HTML and will effectively close unclosed tags for you:

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

Which I fixed by switching to:

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

Herb has since added support for this pattern in https://github.com/marcoroth/herb/pull/1153, but I think this is a case where the refactored code is just better anyways.

We had about 150 cases like this, which you might think would have been pretty painful to refactor. And you would have been right a year ago! But with the recent Claude Opus models, I've had a basically 100% success rate of one-shot fixes simply by pasting in the Herb error. Herb does of course have a `--fix` option as well, but for the cases where it doesn't, AI has done a very effective job.

### Invalid ruby

But some of the bugs were quite serious. Herb caught invalid Ruby in quite a few places:

```html+erb
<% if x.y? && x.z? && %>
```

```html+erb
<% if x? do %>
```

This was pretty surprising to me as we run `erb_lint` on all of our files and have a pretty decent test suite. But we never ran these lines outside of production. Since Herb uses Prism to actually parse the Ruby in ERB files, it caught the issues right away.

## Bugs found in Herb

After passing the linter, I turned to getting our test suite to pass, which revealed a couple bugs in Herb:

### Whitespace bugs

We caught a [few whitespace bugs](https://github.com/marcoroth/herb/pull/1361).

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

### Invalid Ruby

In another, more serious [case](https://github.com/marcoroth/herb/pull/1363), when a comment was on the same line as an `end`, Herb produced invalid Ruby.

```html+erb
<%= render Foo.new do %>
  hello
<% end # comment %>
```

This bug in particular put me in a cold sweat. As I mentioned earlier, we do not run every line of Ruby in CI. As Rails does not compile templates until they are needed at runtime, this kind of bug would be a runtime exception. This is as much an issue with Herb as it is with Rails, as Rails blindly trusts the output of ActionView handlers such as Herb to provide valid Ruby.

While I think we need to add safety measures for this issue to Rails, Marco [added](https://github.com/marcoroth/herb/pull/1259) Ruby validation to `herb analyze`.

### Vendored templates

The invalid Ruby issue becomes much trickier when it comes to ERB provided by gems, such as Primer ViewComponents and dashboard engines from tools like good_job. Currently, all `herb` CLI commands, including `analyze` and the linter, ignore the vendor directory. If a gem includes ERB Herb cannot parse, it could crash production at request time. I've filed [a bug for this issue](https://github.com/marcoroth/herb/pull/1508).

In the meantime, we have a custom CI check that force-compiles all vendored `.erb` files at build time, catching incompatibilities before they reach production. I've also wrote PRs to fix Herb-incompatible ERB in [graphql-ruby](https://github.com/rmosolgo/graphql-ruby/pull/5497) and [Primer ViewComponents](https://github.com/primer/view_components/pull/3850).

### Performance impact

With the linter passing and our test suite green, we were ready to go to production. As a final verification step, we turned on Herb [in a production cluster](https://github.com/github/performance-engineering/issues/1945) we isolate for measuring the performance impact of code changes.

While we saw no impact on runtime performance, we unfortunately saw a significant increase in our boot time, from two minutes to almost three. After some investigation, we identified the cause: Herb takes much longer to compile templates than Erubi does.

Depending on the size of the template, Herb is about an order of magnitude slower than Erubi:

| Template | Size  | Erubi   | Herb       | Added   | Ratio |
|----------|-------|---------|------------|---------|-------|
| Tiny     | 58 B  | 3.9 µs  | 28.3 µs    | +24 µs  | 7.2x  |
| Small    | 250 B | 10.4 µs | 116.1 µs   | +106 µs | 11.2x |
| Medium   | 1 KB  | 24.4 µs | 365.6 µs   | +341 µs | 15.0x |
| Large    | 3 KB  | 81.7 µs | 1,059.7 µs | +978 µs | 13.0x |

In a typical Rails application, a template is compiled from ERB to Ruby when it is rendered for the first time in a process. Subsequent renders hit a cache. Switching to Herb meaningfully increases this cold render overhead, which can become an issue in applications with many templates that are regularly deployed, as the cache must be re-established every the application boots.

In GitHub.com, we use library called [ActionView::Precompiler](https://github.com/jhawthorn/actionview_precompiler/) to warm this cache at boot time, which is why we saw our app take longer to boot (ViewComponent also compiles templates at boot time, also contributing to the slowdown). The precompiler also saves significant memory (around 500mb per container) due to the Copy-on-Write memory usage characteristics of forking servers.

While we've explored a few solutions to the issue, such as a build-time cache similar to Bootsnap, we're currently blocked on using Herb in production until it's resolved. Marco thinks we can optimize Herb to avoid this issue, as Herb hasn't seen much perfromance optimization yet.

In the meantime, I've opened a long-overdue PR to [upstream ActionView::Precompiler into Rails](https://github.com/rails/rails/pull/57234). As an added benefit, having Rails applications precompile templates at boot time will raise Herb parsing errors before they can cause runtime issues.

### Even GitHub doesn't use all of Erubi

But more work remains. The Erubi test suite has 108 tests. Even after all of our work to pass the linter and our test suite, 8 of thsoe 

 Github passed CI with herb on, but 8 erubi tests failed (https://github.com/marcoroth/herb/pull/1548). Even at our scale, we do not use all of the features of Erubi.

## What's next

Dropping ERBLint/ERBLint-github as rules are upstreamed
Adopting more lint rules
inlining render calls
Transpiling to react

## Wrapping up

Really impressed with Marco's work, rapid improvement. Confident it will be a great fit for Rails core, etc.

Give Herb a try! I have no hesitation recommending turning it on for dev and test, where you'll see most of the benefits over Erubi anyways.