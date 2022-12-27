---
layout: post
title: "Accessible from the start"
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

I'm going to share how we're taking this approach to improve the experience of using GitHub for people with disabilities. I'll start by describing the accessibility problem space, share some interesting tooling work, and lastly cover our long-term strategy.

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

## GitHub history 101

To understand how accessibility works at GitHub, I think it's important to start with a little history,mainly because GitHub is a weird company.

For the first six years GitHub was a company, there were no managers. Visitors to our San Francisco headquarters were greeted in a replica of the oval office from the white house. On the floor was a rug that read "the united meritocracy of GitHub."

For years, we operated in what some folks have called a "cooking for chefs" mindset. Since we were developers ourselves, we knew what we'd want GitHub to be like. That meant we could build whatever sounded good to us and reasonably expect our customers to agree. I don't think the manager-less organization structure would have worked for as long as it did if this wasn't the case.



TODO image of rug from https://readwrite.com/github-meritocracy-rug/

## How I think about accessibility

TODO images from https://dev.to/lupitalee/what-is-web-accessibility-2jch, split up into four slides

Explain these images

My experience was, and still is, a form of cognitive disability.


