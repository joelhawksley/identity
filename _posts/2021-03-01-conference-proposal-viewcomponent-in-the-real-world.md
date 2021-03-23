---
layout: post
title: "Conference proposal: ViewComponents in the Real World"
---

_This conference proposal was accepted for [RailsConf 2021](https://railsconf.org) and [RubyDay 2021](https://2021.rubyday.it)._

## Abstract

With the release of 6.1, Rails added support for rendering objects that respond to `render_in`, a feature extracted from the GitHub application. This change enabled the development of ViewComponent, a framework for building reusable, testable & encapsulated view components. In this talk, we’ll share what we’ve learned scaling to hundreds of ViewComponents in our application, open sourcing a library of ViewComponents, and nurturing a thriving community around the project, both internally and externally.

## Details

This talk explores the technical challenges of managing thousands of views and almost half a megabyte of custom CSS in the GitHub monolith. It leans towards the more advanced end of the spectrum, covering topics such as template compilation and static analysis with Abstract Syntax Trees.

It starts by providing detail into the scale of the GitHub application and how it is growing rapidly year over year. This scale has exposed several significant pain points in the developer experience working with the Rails view layer.

For example, it's difficult to figure out which template renders a specific line of HTML. I share how this led us to build template annotations, a feature we upstreamed into Rails 6.1.

Another point of friction covered is getting our application into the right state in local development. I share how we convert our controller tests to system tests at runtime to enable previewing of visual changes in a browser.

I'll also explore the issue of tracing template usage across our thousands of routes. I share how we use static analysis to help developers understand which routes render a template they're editing.

The main technical portion of the talk explores the lessons we've learned building over 400 ViewComponents in the GitHub codebase in the past year.

We'll explore how ViewComponents enable consistency through including logic we traditionally put in view helpers, lead to improved performance through strict controls around database access, manage complexity in how we build our mailers, and enable a quick development lifecycle with Storybook, giving our developers a tool set that makes building UI correctly the default, not the exception.

We'll also cover how we've rolled out this new pattern across dozens of teams and hundreds of engineers, from both the technical and organizational perspectives.

On the technical side, we'll explore the authoring experience, showing how we refactor ViewModels to be ViewComponents.

On the organizational side, we'll cover how we generate our documentation site from YARDoc code comments, provide automated code reviews using a bot, and communicate with non-technical stakeholders.

The end of the talk shifts focus to the open-source aspects of the project. We discuss lessons in empathy, enabling contribution to the project, and how Rails convention has driven the design of the framework.

The talk finishes with a consideration of the bigger picture around the state of ActionView in general, how it might be improved in the future, and how we all need to work together to keep Rails relevant for the long term.

## Pitch

I am the creator and lead maintainer of ViewComponent, GitHub's framework for building reusable, testable & encapsulated view components in Rails. The ViewComponent framework has received significant attention in the Rails community over the past year, and is foundational to several up and coming Rails ecosystem libraries including StimulusReflex.

I'm also the author of the support for 3rd-party component frameworks introduced in Rails 6.1, along with other view-related improvements such as template annotations and the `class_names` helper. In addition, I maintain the Primer ViewComponents library, an open-source Ruby gem of ViewComponents for the Primer Design System.

This talk builds on presentations I gave at RailsConf 2019, sharing a prototype for view components in Rails, and 2020, a technical deep-dive into how a lack of encapsulation affects Rails views. It shares what we've learned scaling up to hundreds of ViewComponents over the past year, including open-sourcing some of them. Through sharing concrete examples from the GitHub codebase, I'll help attendees understand how their applications might benefit from using ViewComponents.

I've already given the talk to our local Ruby group and internally at GitHub, and it's been well-received.
