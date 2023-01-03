---
layout: post
title: "Accessible by default"
---

## Intro

_Warning: This post includes some graphic details of traumatic events._

TODO Photo of Caitlin, Captain and I in front of house from card

In the summer of 2020, my wife, dog and I had moved into the home we hoped to raise a family in. Like many of us in the industry, I lived a comfortable life. A life of privilege. We had little to worry about.

That all changed about a year and half later, at the very end of 2021.

TODO Opener image of day of fire

While we were out of Colorado on a road trip for the holidays, I got a text message from a friend in town about a fire evacuation.

TODO screenshot of emergency evacuation order

We got the evacuation order a little bit before 3pm.

TODO screenshot of Blink alerts

Soon after, falling ash triggered our front door security camera, triggering motion alerts every minute. I had to turn them off. I was regretting having backup power for my modem.

TODO another fire photo, entrance to neighborhood?

Over the course of an afternoon, the news got increasingly dire. Homes were burning in our town, but we didn't know if ours survived.

It wasn't until the following morning that I checked twitter and saw a drone video of our neighborhood.

TODO Drone photo/video

Over a hundred homes in our neighborhood burned to the ground, including ours.

TODO photo of caitlin and I in front of house

For the first time, I saw the world through the eyes of trauma, panic, overwhelm. Our lives were turned upside down.

TODO photo of night walk

One memory that sticks out to me is realizing two weeks later that I hadn't walked Captain since the first. I literally hadn't even thought to do something that I used to do three or four times a day before.

I noticed other things too. It was harder for me to focus. I got angry easily. I remember struggling to use my password manager on my phone. Things that were easy for me to do before were difficult if not impossible.

What I soon learned from a counselor at the Red Cross was that emotional trauma can cause brain damage. In my case, both temporarily and permanently.

This experience has opened my eyes to the privilege I experienced before the fire. It changed the way I view both the world and the work we do in the industry. It inspired me to look for ways to embed empathy into our engineering practices through accessibility-first thinking.

## Table of contents

I'm going to share how we're taking this approach to improve the experience of using GitHub for people with disabilities. I'll start by describing the accessibility problem space, share some interesting tooling work, and some lessons we've learned along the way.

## Who am I?

I'm a staff engineer at GitHub. I work on various company-wide UI-related initiatives. I continue to lead the ViewComponent project.

When I share details of what it's like to work at GitHub, I like to start by giving a rough idea of the scale of our company.

As of December, we have about 4,000 employees. GitHub continues to primarily be built as a monolithic Ruby on Rails application, at least when it comes to serving customer-facing traffic. There are about 1,380 controllers in our codebase.

```
find . -name "*controller.rb" | wc -l
    1029
```

```
find . -name "*controller.rb" | wc -l
    1379
```

I love mentioning this stat every year I give a talk, as it really shows how much we continue to grow our monolith. We've added about 350 controllers in the past year! This is to a code base that is 15 years old and millions of lines of Ruby.

I think it's important to share this kind of context as it can frame why we make the decisions that we do.

## How I think about accessibility

Anyways, back to the script.

TODO images from https://dev.to/lupitalee/what-is-web-accessibility-2jch, split up into four slides

TODO Explain these images. For example, you might have been situationally disabled carrying a stack of pizza boxes into a building today, unable to use your hands to open the door.

There are various guidelines and standards for accessibility, such as WCAG, Section 508, APG, and others. Not all of them agree with each other!

In practice, for the work we do, accessibility means making our applications work with assistive technology. While I won't go into much detail here, we mainly focus on screen readers, tools that read the screen out loud via keyboard control.

And while I can't go into almost any detail, this wouldn't be a talk about accessibility without mentioning that _not_ having an accessible application is a legal risk, and often a significant one.

### GitHub history 101

To understand how accessibility works at GitHub, I think it's important to start with a little history, mainly because GitHub is a weird company.

For the first six years GitHub was a company, there were no managers. Visitors to our San Francisco headquarters were greeted in a replica of the oval office from the white house. On the floor was a rug that read "the united meritocracy of GitHub."

TODO image of rug from https://readwrite.com/github-meritocracy-rug/

For years, we operated in what some folks have called a "cooking for chefs" mindset. Since we were developers ourselves, we knew what we'd want GitHub to be like. That meant we could build whatever sounded good to us and reasonably expect our customers to agree. I don't think the manager-less organization structure would have worked for as long as it did if this wasn't the case.

### The problem space

If you take nothing else away from this talk, it should be that bad accessibility rarely breaks CI. Very rarely do any of our standard practices lead to accessible experiences.

Even when we do have automated accessibilty checks, they are far from perfect. Depending on who you ask, between 30 and 50 percent of accessibility issues can be caught with automation.

For example, we can automatically check that images have alternative text, but we can't check that the alternative text actually describes the image correctly.

There are more subtle issues too. Designers use gestalt techniques such as proximity and scale to convey meaning, information that isn't consumable for people that are visually impaired.

### GitHub's accessibility goals

One of our tenets at GitHub is that we are the "home for all developers." When it comes to accessibility, our goal is pretty simple: Full and equal participation of people with disabilities in the development process. We believe that access to technology is a fundamental human right. That everyone deserves to have the opportunity to create, innovate, and collaborate while contributing to our digital future.

TODO add diagram of letter grades

We measure our progress towards this goal on a letter grade scale. TODO explain letter grades.

These are big goals! Especially for a surface area of thousands of unique user-facing pages.

Because of this scale and how quickly our products are growing, manually checking and fixing each page for accessibility issues is basically impossible. Even if we went that route, pages would likely regress quickly.

## Tooling

To achieve our goals, we need good tools. Here are a couple we use for accessibility: Axe, Previews, and our Forms Framework.

### Axe

Our primary tool is Axe, an automated accessibility scanner. We use Axe across our development lifecycle.

TODO add axe explainer

We turn on axe by default in our local development environment, highlighting issues in red on the page and logging them in the console.

We also run it in production for GitHub staff members who opt-in with a user setting.

We use it in our end-to-end browser test suite that runs against every production deploy.

And perhaps most importantly, we use it extensively to test our UI components in isolation.

### Previews

TODO add lookbook screenshot

When we build our UI components, we write previews for them. A preview is an example of the component being rendered in isolation. So for a button component, we might have a preview for each color scheme option.

We also use these previews in our tests! In ViewComponent TODO add example code etc

What's been fascinating about this workflow has been how much it has blurred the lines between our development and test environments.

I first came up with the idea for working this way when I realized that our test setup and seeds code had a lot of overlap. TODO add example code

What we've ended up doing is consolidating our test cases into previews. We write a preview while designing our components, then use render_preview or visit_preview in our tests. This has a couple advantages:

1) It makes UI tests easier to understand, since you can often just look at the preview and see what is broken. TODO add note about playwright steps?
2) It makes UI components discoverable. At our scale, it's sometimes hard for one team to know what another is building. Sometimes the same thing gets built twice by multiple teams! We use Lookbook and Storybook to organize our previews into a component directory of sorts that can be browsed in local development. I'm hoping we can share it in production some day!
3) It aids collaboration with non-technical stakeholders. Since lookbook runs as part of our Rails app, we can use review apps to share our work with other engineers, PMs, and PWD consultants for accessibility reviews.
4) It couples our tests to our examples. By reusing our test cases as our documentation, there is an incentive to write test cases that exercise our UI code in practical ways. It also ensures that our examples actually work! It was amazing to me the first time we converted our examples to previews and found that a significant fraction of them raised exceptions when rendered! In fact, we are quickly moving away from having documentation sites for components at all, instead leaning on Lookbook for all examples.
5) We can write regression tests with documentation for a11y bugs we catch along the way, Axe can catch less than half of bugs.
6) Most importantly, it allows us to embed accessibility scanning deep into our workflows. In our browser tests, we override every interaction method (such as visit, click, etc) to perform the action and then run an Axe scan (`assert_axe_clean`), failing if there are any results. We display these errors inside Lookbook as well.

This is a great example of how the Rails ecosystem can benefit from adapting ideas from other languages and frameworks.

### Forms Framework

Another critical tool in our accessibility work has been our custom-built forms framework.

TODO insert screenshot of original rails demo from DHH

Forms are a core competency of Rails. If we go back to the original "build a blog in 15 minutes" demo from DHH, most of the demo is form building!

TODO insert screenshot of hotwire demo from dhh

And that's still true! 15 TODO some-odd years later, the hotwire demo is also mostly form building. Obviously this is something that Rails should be excellent at. (Hotwire/Turbo isn't without its own [accessiblity issues](https://github.com/hotwired/turbo/issues/774), either)

And it is! Rails has excellent built-in forms helpers: `form_tag`,  `form_for`, and `form_with` (which combines the first two).

Here is an example straight from the [Action View Form Helpers guides](https://guides.rubyonrails.org/form_helpers.html):

```erb
<%= form_with url: "/search", method: :get do |form| %>
  <%= form.label :query, "Search for:" %>
  <%= form.text_field :query %>
  <%= form.submit "Search" %>
<% end %>
```

```html
<form action="/search" method="get" accept-charset="UTF-8" >
  <label for="query">Search for:</label>
  <input id="query" name="query" type="text" />
  <input name="commit" type="submit" value="Search" data-disable-with="Search" />
</form>
```

What this example makes painfully obvious is that `form_with` more or less maps 1:1 with the resulting DOM. It's essentially a DSL for HTML nodes. This is great! It simplifies a lot of complexity with building forms correctly and gives us a lot of syntactic sugar for things like building lists of select options.

But it isn't accessible out of the box.

Looking at the example code, you can see that the form input has an associated label:

```html
<label for="query">Search for:</label>
<input id="query" name="query" type="text" />
```

This was generated by two separate method calls:

```erb
<%= form.label :query, "Search for:" %>
<%= form.text_field :query %>
```

This example is great because it is accessible! Specifically, passes Axe rule 4.4, [Form <input> elements must have labels](https://dequeuniversity.com/rules/axe/4.4/label), which reads:

> Programmatically associate labels with all form controls. The recommended method for most circumstances is to use the label element and an explicit association using the for and id attributes. [...]

Our example code does this correctly, but there's a problem: it's easy not to do this. As the Axe rule states, all of our form controls need labels. Yet Rails at best gives us an option to provide them.

TODO insert book cover image

One of my favorite engineering books is A Philosophy of Software Design by John Ousterhout. While working on the problem of accessible forms I was reminded of chapter 10, which is titled "Define Errors Out of Existence."

The premise is in the title: we should construct our software to make invalid states impossible!

So about a year ago we realized that we needed to do this for forms. Luckily for me, we had just hired a new engineer on our team who was eager for a fun problem to solve, so I asked him: what would it look like to make our Rails forms accessible by default?

And that's where our forms framework was born. Cameron set off to architect a form builder that avoided common accessibility bugs.

For example, we'd take our previous example:

```erb
<%= form_with url: "/search", method: :get do |form| %>
  <%= form.label :query, "Search for:" %>
  <%= form.text_field :query %>
  <%= form.submit "Search" %>
<% end %>
```

And rewrite it in our new DSL:

```ruby
class SearchForm < ApplicationForm
  form do |search_form|
    search_form.text_field(
      name: :query,
      label: "Search for:",
    )

    sign_up_form.submit(label: "Search")
  end
end
```

What's most important to highlight here is that there is now a single method to create a text field with a label, not two. Under the hood, we generate both the input and label tags, linking them correctly so that Axe 4.4 is satisfied.

So that's some of the tooling work we've done.

## Lessons

As we've rolled out an a11y-first approach to UI development, we've learned a lot along the way.

### Reuse

When it comes to our broader strategy, we've learned that we need to focus on ways of making it only possible to build UI that is accessible. We do this in what has become the standard practice in the industry: components!

Components are just UI abstractions. Reusable pieces.

For our UI teams, this means that our primary success metric is how much our components are used. The more they are used, the less teams need to reinvent accessible patterns.

TODO add datadog explainer of some sort

In practice, we end up needing to focus on two priorities: coverage, the ability for our components to be used to build all of GitHub, and adoptions, whether they are actually used to do so. Both are important but different disciplines.

### Expertise

a11y challenges the notion of full stack development, especially at this level of compliance.

They allow us to spend more time making fewer lines of UI code better. They allow us to keep high standards without expecting everyone to be an expert. Our components have significant, thorough test coverage that would be hard to justify for UI code that is only used once.

### Intractability

In some cases, we've run into UI patterns that simply weren't accessible in any way, sometimes to the point of needing to have an entire page or even an entire workflow redesigned from scratch.

Some patterns aren’t accessible and should be avoided: https://github.com/github/primer/issues/713#issuecomment-1111002165

### Accessibility first

How complicated they should be is an ever-evolving question. Should they be simple, just encapsulating a button? Or should they be more complex, constructing an entire form?

What's been most enlightening about our experience has been that focusing on accessibility has helped us answer a lot of tricky questions like this one. Our current best answer is that components should be optimized for helping developers build accessible experiences. In general, that means we should build components that are complex enough to ensure that they are accessible by default.

TODO add example of nameplate and avatar

Coming from our perspective of having thousands of pages to make accessible, we've seen that it is significantly easier to build accessible experiences if accessibility is the first design priority.

## Conclusion

Universal design is the idea that we should build products, experiences and environments that work for all people regardless of age, ability, or other factors.

TODO insert image of curb cuts

In the real world, a good example of this is curb cuts: while originally intended for wheelchair users, they also benefit stroller pushers and to be honest, those of us who would rather not lift our feet up so high!

TODO insert SSO screenshot

In the software world, this might mean adding a SSO option to our app so that people with disabilities can avoid CAPTCHAs, which are notoriously inaccessible.

By building accessibility practices into the way we build software, we're embedding empathy into our work.

WCAG while it takes work, should just be a starting point. Compliance does not mean usability. Only by building for the users with the greatest needs in mind will we create a world where they can succeed alongside the rest of their peers.

But perhaps the bigger lesson here is that accessibility is just an example of a larger class of blind spots we have as able, wealthy, first-world developers. This reminds me of one of my favorite quotes, from Donald Rumsfeld:

> We also know there are known unknowns; that is to say we know there are some things we do not know. But there are also unknown unknowns—the ones we don't know we don't know. And if one looks throughout the history [...] it is the latter category that tends to be the difficult ones.

Applying this way of thinking has opened my mind to other similar issues. Take browser performance for example: at GitHub, we are issued powerful Apple laptops and cell phones. They enable us to be about as productive as an computer could help us be.

But they give us a false sense of reality: even among our customer base that skews towards users of more powerful hardware, the experience we have using our products is not the same as our customers'.

TODO insert JS benchmark comparison

This is even an issue with request latency! Most GitHub traffic is served from the US east coast, which means that our mostly US-based staff does not experience the lag time our customers in, say, Australia, do.

So how do we look out for these blind spots? How do you find unknown unknowns? By putting yourself in the shoes of others.

So here's what you can do, when it comes to accessibility: use Axe or a similar automated tool. Go without a pointing device for a day. Try a screen reader. And if you can, spend time observing the experience people with disabilities have with what you build.