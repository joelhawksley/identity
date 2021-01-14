---
layout: post
title: "Conference proposal: ViewComponents in the Real World"
---

## Abstract

With the release of version 6.1, Rails added support for rendering objects that respond to `render_in`, a feature extracted from the GitHub application. This change enabled the development of ViewComponent, a framework for building reusable, testable & encapsulated view components. In this talk, we’ll share what we’ve learned scaling to hundreds of ViewComponents in our application, open sourcing a library of ViewComponents, and nurturing a thriving community around the project, both internally and externally.

## Details

## Pitch

I am the creator and maintainer of ViewComponent, GitHub's framework for building reusable, testable & encapsulated view components in Rails. I'm also the author of the support for 3rd-party component frameworks introduced in Rails 6.1, along with other view-related improvements such as template annotations and the `class_names` helper. In addition, I maintain the Primer ViewComponents library, an open-source Ruby gem of ViewComponents for the Primer Design System.

This talk builds on presentations I gave at RailsConf 2019, sharing a prototype for view components in Rails, and 2020, a technical deep-dive into how a lack of encapsulation affects Rails views. This talk will share what we've learned scaling up to hundreds of ViewComponents over the past year, including open-sourcing some of them. Through sharing concrete examples from the GitHub codebase, I'll help attendees understand how their applications might benefit from using view components.
