slidenumbers: true
footer: Boulder Ruby January 2020 - ViewComponents in the real world - @joelhawksley
autoscale: true

## ViewComponents in the real world

![](img/bg.png)

^ Hi

^ My name is joel

^ Thanks for having me

^ Thanks to Rylan, Dan, and Marty for organizing

^ Today we're going to take a peak behind the curtain

^ of one of the biggest, highest-trafficked Rails applications in the world

---

## github.com/github/github

^ github / github / github

^ It seems like every time I give a talk people want to know our stats

^ So here are a few...

---

# 10s of k's requests/second

^ Our app serves tens of thousands of requests per second

---

# ~ two dozen services

^ We have around two dozen services

^ Citadel architecture

^ A lot of them are written in Go

^ optimized extractions from the monolith

^ such as webhook delivery

^ On the rails side...

---

# 580 models

## +144 YoY (33%)

^ `grep -lr "< ApplicationRecord" app/models | wc -l`

^ 580 models

---

# 4573 views

## +702 YoY (18%)

^ `find app/views -type f -name "*.html.erb" | wc -l`

^ 4573 views

---

# 766 controllers

## +206 YoY (36.8%)

^ `find app/controllers -type f -name "*_controller.rb" | wc -l`

^ 766 controllers

---

# 647 jobs

## +107 YoY (19.8%)

^ `find app/jobs -type f -name "*_job.rb" | wc -l`

^ 647 jobs

---
# 397 ViewComponents

## +373 YoY (1554%)

^ `find app/components -type f -name "*.rb" | wc -l`

^ 397 view components

---

# Scaling ViewComponents

^ Today I'm going to talk about what we've learned scaling

^ to hundreds of ViewComponents

---

# Open source

^ share what we've learned open sourcing portions of our UI architecture

---

# Innovation

^ and consider ways to ensure Rails continues to innovate and stay relevant for the long term.

^ PAUSE

---

![40%](img/github-white.png)

^ I've been at GitHub for a couple years now

^ engineer at on Design Systems team

---

[.hide-footer]
![fit](img/primer.png)

^ We are responsible for the Primer design system used throughout GitHub

^ Perhaps our biggest ship just went out recently - dark mode

^ My job on the team

^ to help hundreds of engineers use our design system correctly in our monolith

^ Make building consistent, accessible, resilient UI easy

^ and to generally make building UI an enjoyable experience

^ This is a big challenge!

^ In addition to over 4500 views...

---

# 2015 GET routes

^ We have over two thousand screens in the application

---

^ All need to stay current, even if they're out of the critical path

^ We have a lot of legacy one-off designs that are difficult to maintain.

---
# >450kb of custom CSS

^ Which means almost half a megabyte of custom CSS.

^ This scale makes for some interesting problems.

^ PAUSE

---

^ one example of how I've worked to improve the developer experience

^ is template annotations

---

^ One issue developers had building UI at GitHub was figuring out

^ which template rendered a specific line of HTML

---

^ TODO image

^ for example, when looking at a PR page, if I want to edit this PR badge,

^ how do a I find the right template?

^ I could try searching by the specific class names on the element, but with

^ the functional css approach many apps take these days, this approach is often

^ not very reliable.

---

^ In this case, if we search for the class names on the element, we get dozens of results.

^ It's not super helpful.

^ PAUSE

^ In thinking about this problem, I wondered if it might be possible to add HTML comments

^ at the beginning and end of each template's output, with the path of the template file.

---

^ We did this by writing a custom ERB compiler that added the template path to the output

^ of a template.

---

^ And it worked!

^ We now had a way to quickly figure out which template rendered a part of a page.

^ TODO image/etc https://github.com/github/github/pull/139605

---

^ After seeing the benefits of this patch internally,

^ We extracted it into Rails!

^ It's part of Rails 6.1.

^ TODO image/etc https://github.com/rails/rails/pull/38848/files

---

### `config.action_view.annotate_template_file_names`

^ You can turn it on with the configuration variable X

^ And new Rails applications have it enabled by default in local development,

^ otherwise it defaults to being turned off.

^ PAUSE

---

## Seeds

^ another issue we've run into is getting the application into the right state

^ in local development so we can test visual changes

^ seeds only get us so far.

^ part of this is due to our architecture

---

## Architecture

^ GitHub is a huge application. It's what some people call a citadel.

^ We have a main Rails monolith and about two dozen services.

^ this can make it difficult to get local development into the right state

^ but yet we manage to do it...

^ in our tests.

---
## TDD

^ Unfortunately, we don't have browser-based tests

^ Which means we can't use them for verifying visual changes

^ This is mainly due to how much time it would add to our test suite

^ Which is already over 10 hours without parallelization.

^ However, we do write plenty of controller tests.

^ After numerous pairing sessions helping our designers

^ get their local development environments into the right state,

^ I had an epiphany- what if we could temporarily convert controller tests...

---

## Controller -> System

^ Into system tests?

^ That way, we could reuse all of the existing setup code from our controller tests

^ To preview the application in a specific state to make visual changes

---

^ And that's just what we did!

^ We wrote a module... explain code

^ TODO insert code from system_test_conversion.rb

---

^ Which we then include if `RUN_IN_BROWSER` is appended to a command to run a test.

^ TODO insert code from conditional include

---

^ And here's what it looks like in action...

^ TODO insert gif of run_in_browser

---

^ Unlike template annotations, this hasn't made it into Rails.

^ I'm not sure it's a good idea or not, but it's served us well.

^ https://team.githubapp.com/posts/35123

^ https://github.com/github/github/pull/154697

^ https://github.com/github/design-systems/issues/768#issuecomment-694536798

---

## Seeds vs. test setup

^ But there is something that I think we can learn here.

^ Our seeds and test setup code has a lot of overlap!

^ I'm curious to see if there's ways we could bridge the gap between these conceptual domains.

---

## Static analysis

^ Viewfinder - https://team.githubapp.com/posts/34338

---

^ Third January in a row at Boulder Ruby

^ Going to build on previous talks

^ Following a thread asking a simple question:

---

# Abstractions

^ How can we make Rails views a first-class abstraction?

---

# Problem

^ In general, most of our templates are built by copy-pasting chunks of ERB.

^ We have over 4500 templates in the GitHub codebase, largely built in this way.

^ It's incredibly difficult to make sweeping changes to our view code,

^ limiting the leverage our team has with our design system.

---

# 2019

^ 2019

^ Shared a crazy idea

^ For using Ruby objects to render views

^ Inspired by ideas from React

^ We now call it ViewComponent:

^ A framework for building reusable, testable & encapsulated view components in Rails.

---

# Example

^ Share example component from README

---

# Testing

^ Example test from README

---

# 2020

^ 2020

^ That idea had become my full time job at GitHub

^ Talked about how Rails views work under the hood

^ All execute in the same context, meaning they can share state

---

# Example

^ Previous code, compiled

---

# 2021

^ Today I'm going to share what we've learned scaling to hundreds of components in our application

^ Open sourcing some of those components

^ and building a thriving community around the project

---

# Thinking in Ruby vs. ERB

^ One of the fundamental benefits we've seen writing components

^ Is that they enable us to think in Ruby vs. ERB

---

# Testing

^ this really manifests itself when writing tests

^ force to make you think about what you're writing

^ Unit testing exposes global state dependencies such as current user, which make caching tricky

^ having to declare dependencies is a benefit

^ https://github.com/github/github/pull/139311

---

# Abstractions

^ One of the main lessons we've learned building components

^ Is that they enable us to provide the right abstractions for developers

^ TODO for example, slots for borderbox

---

# Abstractions

^ And perhaps more generally, we need to help developers focus on building products

^ Not implementing the UI.

^ Just like AR simplified use of SQL

^ And controllers made it easy to write code to respond to requests

^ Having an abstraction for building UI.

---

# Super powers

^ Rails is a collection of abstractions that give developers super powers.

^ How does ViewComponent do this in our application?

---

# Consistency

^ As a baseline, it encourages consistency.

^ TODO examples - counter, blankslate - logic and design (counting logic, for example)

---

# Reuse

- TODO for example, sponsors button (https://github.com/github/github/pull/162819)

- TODO for example, reusing code across user/org/business (https://github.com/github/github/pull/158309)

- TODO for example, reusing code across render paths/live reload/etc

---

# Mailers

^ https://github.com/github/github/pull/144469

^ https://team.githubapp.com/posts/34407

^ https://github.com/orgs/github/teams/c2c-actions/discussions/56

---

# Slots

^ LayoutComponent

^ BorderBox

^ Mention blake, jon palmer

---

## Allowed queries

^ https://github.com/github/github/pull/141560/files

^ https://github.com/github/github/pull/158181#issuecomment-705136703

---

## Live editing experiments

---

# Rolling it out

---

## Communication

^ https://team.githubapp.com/posts/33953

^ Weekly initiative updates

^ Internal posts

---

## Linters

^ https://github.com/github/github/pull/143114

^ TODO: sentinel

---

## Refactors

^ Rewrite view model: https://github.com/github/github/pull/166253/files

^ Convert partial to component

^ Add component

---

## WALL-E

^ Six people

^ Stats

^ TODO bin/rails test test/fast/linting/component_usage_test.rb

---

## Extraction

^ Properly built components are more likely to be useful outside of one app

^ We introduce components inside the monolith, then extract

^ Team post: https://team.githubapp.com/posts/34739

---

## Primer ViewComponents

^ We now have a library of ViewComponents

^ Open sourcing forced us to do work we should have done a long time ago

^ Intern manuel

---

## Autogenerated docs

^ https://github.com/primer/view_components/pull/94

^ https://primer.style/view-components/

^ Lesson: Open source project updates consumed internally

^ Have to treat internal projects as open source due to scale docs test coverage etc

---

## Storybook

---

# Two abstractions

^ There is one problem with this approach that I can't shake:

^ It means that we now have two ways of writing views that work differently

^ Granted, we already had this problem with using ViewModels,

^ But I can't imagine Rails having native support for ViewComponents,

^ At least as they exist today in a separate directory.

^ TODO xkcd comic on standards

---

# What to extract?

^ But maybe we could extract some of what makes ViewComponent useful into Rails!

^ TODO One example is the pretty partial GEM

^ Could VC feel as light as views? Could we have ruby objects in the Views folder?

---

^ PAUSE

---

# OSS

^ The ViewComponent project has been very successful.

^ We've averaged one release a week since publishing the project in August 2019.

^ We've had contributions from over 80 developers, only a dozen of which work for GitHub.

---

# Empathy

^ This is my first time running an open source project

^ It's been a huge lesson in empathy.

^ We've been lucky to have a lot of engagement on the project.

^ And what's stuck out to me is that in every issue, PR, or discussion posted

^ There is something to be learned to improve the framework. Even the small stuff.

---

^ If someone was confused by the documentation and wrote a component incorrectly,

^ it's evidence we can use to improve our docs.

---

^ TODO insert other examples, twitter quote about us doing it right

^ Another lesson I've learned is how powerful Rails convention is.

---
# Convention

^ When writing ViewComponent

^ we aimed to conceptually align the framework with Rails as much as possible.

^ Rails conventions mean baseline expectations outside framework

^ And because of that, it's enabled others to almost instinctively know how to contribute

---

^ TODO for example, previews

^ TODO for example, caching

^ The strong conceptual foundation provided by Rails has enabled us to make good design decisions.

---

# Enabling contribution

^ Another thing we've focused on is enabling contribution.

^ We want to enable people to make high-quality contributions as easily as possible.

^ The library isn't super complicated,

^ but it has some nuance and differing behavior across Rails versions.

^ One way we've reduced the burden of this is through matrix builds

---

# Matrix builds

^ By running the test suite against over a dozen combinations

^ of Ruby and Rails, we're able to ensure every change works across all the of those combinations

^ But perhaps more importantly...

---

# Test coverage

^ It's enabled us to ensure we have 100% test coverage,

^ By combining coverage data from all of the matrix builds

^ Having a confident foundation like this makes it easier to accept contributions.

^ I will note that this hasn't prevented a couple performance regressions

^ But we're working on tooling to prevent those too.

^ https://github.com/github/view_component/pull/424

---

# Design from experience

^ Lesson: Design from real experience, not hypothesis

^ One missing feature is caching

^ We don't do view caching, so it's more difficult for us to build the framework support for it

---
# Innovation

^ Another thing this project has made me think about is innovation in Rails.

---

# Dilemma

^ There is a theory called the innovator's dilemma.

^ TODO innovator's dilemma cover

---

> The Innovator's Dilemma is the decision between catering to current needs, or adopting new innovations and technologies which will answer future needs.

^ READ QUOTE

^ Rails is a very mature.

---

# Dependency

^ GitHub's survival is ultimately pretty dependent on Rails' ability to stay relevant.

^ We have so much built on top of Rails

^ it's very unlikely we'd rewrite our core application.

---

# Survival

^ Which means that Rails' survival, is our survival.

^ So what does that mean for all of us?

---

# Innovate

^ We need to innovate!

^ Improving Rails is the only way we'll survive.

---

# Citizenship

^ We need to take ownership of keeping Rails relevant for the long term.

^ By being good citizens. By participating.

^ Rails was built by people just like all of you

^ And we benefit from the work they've put in

^ You can see this in GitHub's contributions to the framework

^ but we need more voices.

---

## Mining for abstractions

^ mining existing applications for abstractions for rails