---
layout: post
title: "Conference proposal: How to make your application accessible (and keep it that way!)"
---

## Abstract

Our industry is shockingly bad at accessibility: by some estimates, over 70% of websites are effectively unavailable to blind users! Making your app accessible isn’t just the right thing to do, it’s the law. In this talk, we’ll share what it’s taken to scale GitHub’s accessibility program and equip you to do the same at your company.

## Details

This talk explores the problem space of making an existing Ruby on Rails application accessible, using the GitHub.com monolith, one of the biggest Rails code bases in the world, as an example. It shares an honest look at our successes and failures.

I begin the talk by discussing the poor state of web accessibility and how as a Ruby community that prides itself in being inclusive and welcoming we have a lot to improve on.

I introduce the talk as a follow-up to my talk last year based on an especially fruitful Q&A after I gave it. The discussion focused on three questions: How do you get leadership to care about accessibility? How do you make an entire application accessible? How do you keep it that way?

I then provide context on the scale of GitHub and why we are pursuing accessibility goals: legal and economic issues. I share that there are three core competencies that have made us successful when we had failed many times before: measurement, durable ownership, and lived experience.

For measurement, I discuss the never ending nature of trying to refactor a large codebase like ours. I share how we use measurement to propose and execute large scale changes and how metrics help leadership see progress towards those goals.

For durable ownership, I show how we use a service catalog to ensure teams across the company are held accountable for the accessibility of their parts of our product. This system is also what we use for security and availability accountability, and it helps us manage ownership as teams, projects, and code comes and goes.

For lived experience, I share how pivotal it was to hire a person with lived disability experience and to give them power to change our company. I highlight this decision as the most critical turning point in making GitHub accessible. I provide the audience with example user stories they can take home and implement in their products to bring the lived experience perspective to the accessibility of their applications.

In conclusion, I implore the audience to make their applications accessible, not just because it is the law, but because it's the right thing to do if we don't want to leave people with disabilities behind during a time of incredible technological progress.

## Pitch

I am a staff engineer at GitHub, working on user interface architecture and strategy. I am the lead engineer on our effort to make GitHub accessible for all developers.

I am the creator and lead maintainer of ViewComponent, GitHub's framework for building reusable, testable & encapsulated view components in Rails. The ViewComponent framework has received significant attention in the Rails community, and is foundational to several up and coming Rails ecosystem libraries including StimulusReflex.

I'm the author of the new Strict Locals feature in Rails 7.1. I'm also the author of the support for 3rd-party component frameworks introduced in Rails 6.1, along with other view-related improvements such as template annotations and the `class_names` helper.

This talk builds on previous RailsConf talks I've given for the past 5 years: In 2019 I shared a prototype for view components in Rails, in 2020 I gave a technical deep-dive into how a lack of encapsulation affects Rails views, in 2021 I shared what we learned scaling up to hundreds of ViewComponents, in 2022 I explored our successes and failures taking on our significant CSS technical debt, and in 2023 I shared how we are building accessible-by-default tooling into our UI stack.

I've already given the talk to our local Ruby group and internally at GitHub, and it's been well-received.
