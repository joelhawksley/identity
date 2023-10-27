---
layout: post
title: "Conference proposal: Accessible by default"
---

_This proposal was accepted for [RailsConf 2023](https://railsconf.org) and [Rocky Mountain Ruby 2023](https://youtube.com/watch?v=8tR3LJ2cEsE)._ [Download slides](/talks/2023-accessible-by-default/slides.key) [View blog post version](/2023/04/21/accessible-by-default.html)

## Abstract

It's one thing to build a new application that meets the latest accessibility standards, but it's another thing to update an existing application to meet them. In this talk, we'll share how we're using automated accessibility scanning, preview-driven development, and an accessibility-first form builder to make GitHub's 15-year-old, 1,400-controller Ruby on Rails monolith accessible.

## Details

This talk explores the problem space of making an existing Ruby on Rails application accessible, using the GitHub.com monolith, one of the biggest Rails code bases in the world, as an example. It shares an honest look at our successes and failures.

I start by sharing how I gained a new perspective on accessibility work through a cognitive disability brought on by the trauma of losing my home in a wild fire. I talk about how I struggled to use technology I was familiar with before.

I give a quick overview of how I reason about accessibility, using the situational, temporary, permanent framework that shows how most people have a situational disability, and thus need for accessibility affordances, on a daily basis. For example, one might need to use a door opener button when their hands are full of packages.

I then give a quick vignette about how GitHub did not have managers for a long time, leading to a culture that incentivized people to build what they needed for themselves, not for others not like them. I explain how we've set company goals to change these norms, but that we need to make tactical changes too.

For the technical portion of the talk, I share three techniques we've used to improve our accessibility.

First, I share how we use the Axe automated scanner in practice, with a custom ruleset shared across a browser plugin, local development, and our test suite.

Second, I share how we use a novel approach to building previews for our UI code, de-duplicating our test and development environments and creating a test target for automated scanning.

Third, I share how we've built a custom form builder that has accessible defaults baked in, removing certain error states from existence.

Then, I share several key lessons from putting these tools into practice:

First, I explain how some UI patterns are incredible difficult to make accessible. I share examples of patterns we've avoided due to accessibility concerns.

Second, I share how this higher level of attention to detail is only possible through reuse of common UI elements, and that our component abstractions should be driven by units we can make accessible by default.

Third, I share how accessibility has challenged our notion of what a full stack developer should be. While we might be able to expect every developer to be able to empathize with every disability, we can't expect everyone to be able to solve every accessibility problem.

I conclude the talk by sharing how accessibility improves the world for everyone, giving the real-life example of curb cuts. I then given a parallel example of how SSO can help people avoid CAPTCHAs, a pain point I had.

I then expand the aspiration of the talk to discuss the greater issue of blind spots in our industry practices and how accessibility is but one example of how we have empathy gaps on a daily basis.

## Pitch

I am a staff engineer at GitHub, working on user interface architecture and strategy. I am the lead engineer on our effort to make GitHub accessible for all developers.

I am the creator and lead maintainer of ViewComponent, GitHub's framework for building reusable, testable & encapsulated view components in Rails. The ViewComponent framework has received significant attention in the Rails community, and is foundational to several up and coming Rails ecosystem libraries including StimulusReflex.

I'm the author of the new Strict Locals feature in Rails 7.1. I'm also the author of the support for 3rd-party component frameworks introduced in Rails 6.1, along with other view-related improvements such as template annotations and the `class_names` helper.

This talk builds on previous RailsConf talks: In 2019 I shared a prototype for view components in Rails, in 2020 I gave a technical deep-dive into how a lack of encapsulation affects Rails views, in 2021 I shared what we learned scaling up to hundreds of ViewComponents, and in 2022 I explored our successes and failures taking on our significant CSS technical debt.

I've already given the talk to our local Ruby group and internally at GitHub, and it's been well-received.
