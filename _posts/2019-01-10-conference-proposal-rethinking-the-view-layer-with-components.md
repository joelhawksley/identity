---
layout: post
title: "Conference proposal: Rethinking the View Layer with Components"
---

_This conference proposal was accepted for [RailsConf 2019](https://www.youtube.com/watch?v=y5Z5a6QdA-M) and [RubyConf Taiwan 2019](https://www.youtube.com/watch?v=MGAs0QALAiM)._ [View slides](/talks/2019/slides.md)

## Abstract

While most of Rails has evolved over time, the view layer hasn’t changed much. At GitHub, we are incorporating the lessons of the last decade into a new paradigm: components. This approach has enabled us to leverage traditional object-oriented techniques to test our views in isolation, avoid side-effects, refactor with confidence, and perhaps most importantly, make our views first-class citizens in Rails.

## Details

We’re going to talk about the shortcomings of the current Rails approach to views. We’ll then look at how React has introduced new ways of thinking about views. We’ll show how we’ve begun to incorporate these ideas into Rails, and how it might change the way Rails views look in the future.

The talk is based around the story of how we refactored an existing ERB template from the GitHub application into Ruby classes that function much like React components.

I will talk about how the original template:
- Is hard to test efficiently
- Is impossible to measure with code coverage tools
- Leads to over-fetching / heavy requests due to ActiveRecord
- Fails basic Ruby code standards

And through the talk, I will refactor the partial into Ruby classes that:
- Are tested efficiently, in isolation
- Are audited using standard code coverage tooling
- Only receive the data they need
- Comply with Ruby standards and idioms

I will then discuss how we’ve used this approach at GitHub and some of the performance implications.

This talk will fall on the intermediate level. It is a classic case of applying ideas from one technology (React) to another (Rails). It is a mix of both practical takeaways and a conjecture on the future of Rails.

## Pitch

I’ve worked on Rails apps of all shapes and sizes, but working on GitHub, a 10-year-old monolith with almost 4000 view files, has changed my perspective on the Rails view architecture. This talk will share this change in perspective in a way that is both interesting and practical, showing how we’ve applied this new way of thinking about views to one of the biggest Rails codebases in the world.