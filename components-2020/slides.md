autoscale: true
slidenumbers: true
theme: Simple, 1
text: Avenir Next Medium, #24292e
text-strong: Avenir Next Bold, #24292e
header: Avenir Next Medium, #24292e
header-strong: Avenir Next Bold, #24292e
code: Menlo Regular, #6f42c1, #005cc5, #0366d6, #d73a49, #d73a49
background-color: #ffffff;

<!--

The Missing Abstraction

Rails is missing an abstraction, and it's hiding in plain sight, right inside your application. 

Goals of talk:

- Inspire audience to think about how they can contribute to Rails
- Educate audience on how the Rails view layer works today
- Inspire audience to consider component - driven architecture

Pitch:
I'm a software engineer at GitHub, working on one of the largest, most-trafficked Ruby on Rails applications in the world. My talk on the initial prototype of ActionView::Component was the third-most popular of RailsConf 2019 based on YouTube views.


-->

# [fit] The Missing Abstraction

^ How can I be relaxed?

---

# Hello!

^ Name

---

# [fit] Joel Hawksley
# hawksley.org

^ Name is Joel

^ And I...

---

^ Microsoft logo

---

![100%](img/github.png)

^ work at GitHub

---

^ We're a distributed company, which means that I do most of my work at my home in Boulder, in my pajamas.

---

^ It also means that you guys are the first non-canine mammals I've been in contact with today!

^ ??Picture of captain

---

^ I do most of my work on what has to be the best named codebase in the world:

---

# github.com/github/github

---

^ PAUSE

---

# Thanks

^ moment of gratitude

---

^ PAUSE

---

^ Rails is missing an abstraction.

---

^ It's clear to me now, but that hasn't always been the case.

---

# Etc

^ Helpers

---

# TeeSpring

^ Decorators

^ Explain pattern

---

# Galvanize

^ react-rails

^ explain pattern

^ isolation testing

---

# Cells

^ Explain pattern

^ Current things don’t render, except for cells :)

---

# GitHub

^ Presenters

^ explain pattern

---

^ When I joined GitHub, I remember something @eileencodes said early on: If it doesn't have to do with our business, it needs to go in Rails.

^ In other words, our mindset was to be "upstream by default"

---

^ Why do we do this?

^ We didn't always work with stock Rails.

^ In fact, up until 2018, we were on long running forks of both Rails and Ruby.

---

^ The maintenance burden of this arrangement grew over time to be unsustainable.

---

^ It's clear that a lot of us are dealing with this.

---

^ Gems like Draper and Cells have _millions_ of downloads.

---

^ Every Rails app I've worked in has done something similar

^ Whether using these gems or rolling something custom.

---

^ Rails backpack analogy

---

^ Decision you shouldn’t have to make

---

^ Set out to collect these ideas and think about what it might look like to bring them into Rails.

---

# How Rails views work today

^ How rails views work today
^ Single module
^ List number of methods defined dynamically on GH app
^ Why this is bad
^ encapsulation

---

# ActionView::Component Prototype

^ What we do is the best:
^ Encapsulating into a single object
^ Easier to make fast
^ Better than partials and helpers
^ Instance variable context encapsulation

---

^ superset of the rails view layer
^ Works exactly as you’d expect it to

---

# Performance

^ Requests per second

^ It works for us

---

# Rails Patch

^ In June, we landed a patch in Rails that added support for `render_in`

^ Support from Rafael

---

# Gem

^ In August, we published version one of the `actionview-component` gem, extracting the library from `github/github`

---

^ Since then, we've shipped X releases

---

^ With a large majority of contributions coming from the Rails community

---

^ Blown away by support

^ My first open source project

^ We've added a bunch of features

---

# Generators

^ Kasper ?

---

# Previews

^ Juan Manuel Ramallo

---

^ Similar to ActionMailer::Previews

---

---

# Lessons of the past year

---

## Migration path

^ “If it could be a partial, it could be a good component”

---

# Thanks

^ Slide of all contributors
