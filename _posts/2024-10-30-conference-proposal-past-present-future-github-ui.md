---
layout: post
title: "Conference proposal: The Past, Present, and Future of GitHub.com UI"
---

## Abstract

"Those who cannot remember the past are condemned to repeat it." -

The way we build UI for GitHub.com gone through several major changes over the lifetime of the codebase. We've used CoffeeScript, jQuery, Web Components, ViewComponents, and React. In this talk, we will share key learnings from these changes, address common questions about the state of UI at GitHub, and explore the future of UI practices in applications big and small, lest we continue to repeat the mistakes of the past.

Intro
  - My name is Joel, I'm a staff engineer at GitHub. My colleague Jonathan Fuchs and I are the closest thing GitHub has to UI architects.
  - Slides are available at this link if you want to follow along

Past
- Relaxed, testing philosophy in on boarding docs
- Removal of system tests
- Staff ship testing for UI changes
- 180 settings pages, copied and pasted

Present
- Staff ship doesn’t test long tail
- Increased availability standards
- https://antithesis.com/docs/introduction/why_antithesis/ - Framing of catching bugs before customers do
- Paradox of success for design system - the more it's used, the bigger the splash radius of changes, making it harder to change with the same level of resiliency

Future

Key takeaways
  Work is never done, wholesale migrations impossible
  Technical changes need to be justified by a business need, such as competition
  Modern UI work is harder than backend
    Numerous states to account for (a11y, runtime targets (browser, device CPU/RAM, connection))
    Bad design doesn't break CI
  Need to constantly fight complexity
  Accessibility and availability is same as security
  Lack of convention for UI compared to Rails backend practices
    Cost of re-inventing the same UI patterns across the industry

Parking lot
  Name each era/chapter? "bootstrap", "primer CSS", "copy-pasta"