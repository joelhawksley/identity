---
layout: post
title: "Accessible by default"
---

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

I noticed other things too. It was harder for me to focus. I got angry easily. I remember struggling to use my password manager on my phone.

What I soon learned was that emotional trauma can cause brain damage. In my case, both temporarily and permanently.

This experience has opened my eyes to the privilege I experienced before the fire. It changed the way I view both the world and the work we do in the industry. It inspired me to look for ways to embed empathy into our engineering practices through accessibility-first thinking.

## Table of contents

I'm going to share how we're taking this approach to improve the experience of using GitHub for people with disabilities. I'll start by describing How I think about accessibility, share some interesting tooling work, and lastly cover our long-term strategy.

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

Explain these images

My most acute trauma symptoms after the fire were a temporary disability. These days, there are some lingering effects that are likely permanent. I'm fortunate that they are minimally uncomfortable at this point.

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

To achieve our goals, we need good tools.

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

I first came up with the idea for working this way when I realized that our test setup
