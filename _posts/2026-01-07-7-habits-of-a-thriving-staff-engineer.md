---
layout: post
title: 7 Habits of a Thriving Staff Engineer
---

Beyond Senior: Life at Staff
Beyond Senior: Considering the staff path

_A transcript of my 2026 talk, as presented at Boulder Ruby._

Abstract
  You’re at senior, but you’re hungry for more. What’s next? In this talk, we’ll attempt to define the staff-plus role and help you decide if it's for you.

Intro
  For many software engineers, the senior role is a crossroads. At many companies, it's the highest you can go as an individual contributor. You basically have one option for promotion: management. But it doesn't have to be this way. Your journey as an individual contributor doesn't have to stop at senior. There is another path: staff-plus.

  A little over a year ago, Jesse from Stripe gave a talk here about what it means to be a senior engineer. At the time, I took a mental note about doing a similar talk for the staff level.

  This past year, I took paternity leave to bond with our second child. In my time away from work, I spoke at Rocky Mountain Ruby. It was great to see many of you there! At the speaker dinner the night before the conference, I was chatting with Becki about our jobs as staff engineers and we quickly realized how different they were!

  Many of my conversations with fellow staff engineers both at GitHub and elsewhere take this turn. Even with a shared language of Will Larson's staff engineer archetypes, it can be disconcerting to try to relate to others in the role, let alone learn what it takes to thrive in it.

  I've been a staff engineer for four years now. I am regularly asked: What is your job? How do I get promoted to staff? Do I want to be a staff engineer? Today I'm going to attempt to answer those questions, based on my experience and conversations I've had with other staff engineers inside and outside GitHub. My selfish goal is that you'll poke tons of holes in everything I have to say so that you can help me improve my practice!

  Of course, what I'm sharing here is just my opinion and not that of GitHub's or any of my previous employers.

  Before I get to far, a quick survey: how many people here would call themselves Junior? Senior? Staff plus?
Table of contents
  How I got to staff
  Attempt to define role
    I'll start by trying to define the role with examples from my experience,
  Tips and tricks
    then share a collection of habits I believe are critical to thriving as staff.
How I got here
  I got into software engineering through the side door. After a short but thrilling career as a news photographer, I started my career at MojoTech (a software consultancy) first as a level-one apprentice. From there, I promoted to "developer", no prefix. Another year later, I was promoted to "lead developer," which was more or less Senior. There were no levels beyond that.
  At my next job, a startup, I was hired at and remained at Senior.
  A year later, I left for another startup. My title was also Senior. Six months later, I was promoted to Lead Engineer. There were maybe two dozen engineers and as a Lead, I reported to the VP of engineering. I had one engineer who reported to me.
  6 months after that, I joined GitHub as a no-prefix "engineer", ostensibly going down two levels, but for decent pay increase. GitHub had a few hundred (maybe ~300) engineers at the time. We had a total of eight engineering levels: Intern, 1/2/3, Senior, Staff, Principal, and Distinguished. Our system remains more or less the same today with ~1,000 engineers.
  My path to a staff role at GitHub started a couple of months into the job. I had the idea for ViewComponent and I pitched it to my manager Zaid, who gave me 20% time to pursue it. After a few months, I had a working prototype, which was the basis of my first presentation at Boulder Ruby!
  A year and a half after I joined, I was promoted to senior in large part due to the ViewComponent project. While at an all-company offsite, I pitched Diana, the leader of the design systems organization, on building out our design system in ViewComponent. A few months later, I asked to join her team to work on ViewComponent full time, which was granted. That year was 2020. As the summer rolled around, there was a request for proposals for projects to address technical debt in our monolith, and I proposed having folks build and adopt ViewComponents for our design system to increase the consistency and quality of our user interfaces. I ended up leading a "virtual team" of about a dozen engineers for half the year, building and adopting ViewComponents. The following spring, I was promoted to staff for this work, about three years after joining GitHub. I have since reported to six different directors in the past five years.
Defining the role
  What makes a engineer staff? Well, it's not senior. And it's not principal. Perhaps it's best to use the term staff+ to encompass the roles beyond senior. In my experience, the staff level is _beyond_ terminal, in that it's totally OK to never go beyond Senior for your entire career.

  In general, staff engineers work at a broader _scope_ than senior engineers, in breadth or depth.

  While a senior engineer typically works at the team level, a staff engineer might work on problems that span multiple teams, potentially across different organizations. They might even report to a director instead of a team-level manager.

  Or, they might go deep. One analogy we use for technical depth at GitHub is about rope:

|   |   |
|---|---|
|Junior         |Learns about rope                                  |
|Mid            |Can tie basic knots                                |
|Senior         |Calculates rope strength, knows a lot about knots  |
|Staff          |Understands rope making                            |
|Principal      |Knows more about rope than you ever will           |
|Distinguished  |Invented Nylon                                     |

> https://rewards.aon.com/en-us/insights/compensation-101/how-much-to-pay-rewards-program-design

  Or, they go long. They might work on problems that take months or even years to solve.

  Perhaps the best definition of the staff+ role is the archetypes from Will Larson's Staff Engineer: Tech Lead, Architect, Solver, Right Hand.

  A Tech Lead "guides the approach and execution of a particular team. They partner closely with a single manager, but sometimes they partner with two or three managers within a focused area. Some companies also have a Tech Lead Manager role, which is similar to the Tech Lead archetype but exists on the engineering manager ladder and includes people management responsibilities." I've done this four times now at GitHub, each time covering for the absence of one of my Director's managers'. I've taken the Tech Lead Manager role, doing 1:1s with reports, serving as a hiring manager, and even helping with yearly reviews.

  An Architect "is responsible for the direction, quality, and approach within a critical area. They combine in-depth knowledge of technical constraints, user needs, and organization level leadership." Most of my work on ViewComponent at GitHub has fallen into this bucket.

  A Solver "digs deep into arbitrarily complex problems and finds an appropriate path forward. Some focus on a given area for long periods. Others bounce from hotspot to hotspot as guided by organizational leadership." My initial work on ViewComponent was this. I worked with Aaron Patterson to develop a novel solution and wrote the upstream patch in Rails to make it work without a monkey patch.

  A Right Hand "extends an executive’s attention, borrowing their scope and authority to operate particularly complex organizations. They provide additional leadership bandwidth to leaders of large-scale organizations." This is a role I've fallen into a lot. For example, I wrote the initial draft of my director's quarterly/semester/yearly/multi-year plans, surfacing ideas proposed by IC engineers in our organization. I spent half a year doing this for the Accessibility effort at GitHub. For example, I was given the ambiguous task of defining our strategy for prioritizing which parts of our application to audit and remediate first. I used our data warehouse to produce a report showing the distribution of traffic across our 2,000+ pages, highlighting which pages were used by the average user in a given week. We identified a few dozen product areas and prioritized working with those teams.

  So that's how I see the role. More scope, playing a particular archetype. Sounds pretty fun, right? I think so. Now here are some habits that have helped me along the way.
Habits
  Align with archetypes
    I like to use the archetypes to align with my manager to make sure our expectations are the same for a given project. I think this is true of all levels, really. We should be regularly validating that our manager agrees with how we think about our work. Something I've struggled with along these lines is seeing other staff engineers do impressive things in other archetypes and feeling like an imposter for not being like them. This is nearly always the case, as there is rarely a business need for two staff engineers that do the same thing.

    It also speaks to a conundrum I've seen many seniors looking for promotion struggle with: there has to be a business need for a staff role. So if you're on a team with other staff engineers, it's generally harder than if no one else is staff. I'll be the first to admit that it was to my advantage to be the first staff engineer under my promoting director. Either, there might not be any staff-level work in your area, or even your company!
  Predict the future
    Part of having impact at a breadth and depth beyond senior is looking towards the future. What are the internal trends (technical and non-technical) that could affect our part of the company? What about external trends? Are there new technologies we should experiment with? What is our competition doing technically that could make our customers want to use their product? To avoid drinking from the firehose that is Twitter/Bluesky/Hacker News, I subscribe to the Hacker Newsletter, Ruby Weekly, and other topic-specific newsletters (such as accessibility news). This was especially important when working on accessibility as the legal landscape is constantly evolving in that area.
  Speak truth to power
    As an IC, I've often had moments where I felt like leadership didn't care enough about what I cared about. Whether it was code quality, tech debt, software craftsmanship. I see part of our job as staff engineers as representing the technical concerns of the engineering discipline to people in power outside of engineering. To be a check and balance on the product discipline by surfacing and justifying engineering-driven priorities. How to do this depends greatly on the situation, but using data is a way of creating a shared understanding of a problem.
  Disambiguate, then delegate
    Build conceptual consensus
    Not consensus. Shared mental models. bruce - what is the problem here? how will we know we've solved it?
    CSS modules example - knew we wanted to leave styled components, decided to use CSS modules. Tasked with migrating all components and dotcom code without breaking anything. Delegated work to others in phases and chunks
    Solving ambiguity through research, proofs of concept, reading papers, trying new technologies (CSS layers) connecting with industry peers
  Keep a journal
  Generate energy
    Keeping the rhythm
    Organizing complex moving parts of large migrations
    ViewComponent migration project was a big part of my staff packet

Get asked to weigh in on things a lot, need to be careful pulling rank. Sometimes management wants you to break a tie

With so many different archetypes, it's really easy to feel like you aren't doing enough

Able to be relied on to deliver
  responsive
  dark mode

Up or out pressure

Early or late promo
  some people don't press for it
    at some point you become so senior that it's unfair for new seniors to have the same title

Good reviews
  "wealth of knowledge"
    should learn something in interviews

Unequal opportunity
  Better project leads to better perf
  Risky to take promo if only short term need
  Team might not need staff work
  Or even company

Good perf
  Hit a lucky spot with CSS modules

Bad perf
  Very few critiques

promotions through mentoring and pairing on regular basis examples
hiring - served as hiring manager
contractors
Read all performance reviews for references and anecdotes
"invented rope"
Mention Levels.fyi

Inflation-adjusted numbers (fall 2025):
Apprentice making about $70k
Developer making about $85k
Lead Dev making about $110k
Wunder senior, but made $136k
Galvanize senior, making $166k
GitHub mid, $210k
GitHub senior, $275k
GitHub staff, $345k