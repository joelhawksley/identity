---
layout: post
title: "Conference proposal: Breaking up with the bundle"
---

## Abstract

Over the course of 14 years, the GitHub.com CSS bundle grew to over 30,000 lines of custom CSS. It became almost impossible to refactor. Visual regressions were common. In this talk, we'll share an honest picture of our successes and failures as we've worked to break up with our CSS bundle by moving towards a component-driven UI architecture.

## Details

This talk explores the past, present, and future of custom CSS in the GitHub.com monolith, one of the biggest Rails code bases in the world. It paints an honest picture of how we have tried and often failed to get ahead of our CSS technical debt.

I start by showing how our custom CSS has grown over the past 14+ years, despite having a design system! I then explain how new custom CSS is the baseline success metric I have for our design systems engineering team.

I then talk about how CSS is a pit of failure, giving examples of how we've introduced visual regressions and how it's difficult to test for bad designs. I show how CSS lacks the kinds of tools we use to write maintainable, changeable software in other languages.

I then explain the main reason why custom CSS is a problem for GitHub: it's making our frontend hard to change, something we so badly want and need to do to continue to innovate as a company. This is no small matter.

I set up the rest of the talk by explaining how I will share what we've done to try to mitigate problems with our custom CSS.

I share specific examples around:

- Measuring technical debt to communicate the problem effectively to leadership and to help other teams contribute to our work
- Attempting (and failing) to split our CSS bundles by functional area
- Attempting (and succeeding) to isolate and encapsulate custom CSS
- Building a new way of testing for visual regressions with snapshot testing of computed styles with the Chrome Devtools Protocol

I then conclude the talk with my big-picture takeaway from this work: That ideas should not be conflated with technologies. What makes React great can and should be adopted in the Rails ecosystem.

## Pitch

I am a staff engineer at GitHub, leading GitHub's work on addressing our significant frontend technical debt.

I am the creator and lead maintainer of ViewComponent, GitHub's framework for building reusable, testable & encapsulated view components in Rails. The ViewComponent framework has received significant attention in the Rails community, and is foundational to several up and coming Rails ecosystem libraries including StimulusReflex.

I'm also the author of the support for 3rd-party component frameworks introduced in Rails 6.1, along with other view-related improvements such as template annotations and the `class_names` helper. In addition, I maintain the Primer ViewComponents library, an open-source Ruby gem of ViewComponents for the Primer Design System.

This talk builds on previous RailsConf talks: In 2019 I shared a prototype for view components in Rails, in 2020 I gave a technical deep-dive into how a lack of encapsulation affects Rails views and in 2021 I shared what we learned scaling up to hundreds of ViewComponents. This talk gives an honest picture of our successes and failures taking on the significant CSS technical debt we've encountered as we move towards a component-driven view layer.

I've already given the talk to our local Ruby group and internally at GitHub, and it's been well-received.
