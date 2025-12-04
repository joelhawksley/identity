---
layout: post
title: Beyond Senior: Consider the staff path!
---

_A transcript of my 2026 talk, as presented at Boulder Ruby._

_You’re at senior, but you’re hungry for more. What’s next? In this talk, we’ll attempt to define the staff-plus role and help you decide if it's for you._

For many software engineers, the senior role is a crossroads. At many companies, it's the highest you can go as an individual contributor. You basically have one option for promotion: management. But it doesn't have to be this way. Your journey as an individual contributor doesn't have to stop at senior. There is another option: staff.

A little over a year ago, Jesse from Stripe gave a talk here about what it means to be a senior engineer. At the time, I took a mental note about doing a similar talk for the staff level.

A couple of months ago, I spoke at Rocky Mountain Ruby. It was great to see many of you there! The night before the conference, I was chatting with Becki about our jobs as staff engineers and we quickly realized how different they were!

I am regularly asked: How did you get promoted? What is your job? How do I get promoted to staff? Do I even want to be a staff engineer? Today I'm going to attempt to answer those questions, based on my experience and conversations I've had with other staff engineers inside and outside GitHub. My selfish goal is that you'll poke tons of holes in everything I have to say so that you can help me improve my practice!

Of course, what I'm sharing here is just my opinion and not that of GitHub's or any of my previous employers.

Before I get too far, a quick survey: how many people here would call themselves Junior? Senior? Staff plus?

## Table of contents

Let's break this into three sections: How I got to staff, defining the role, and some strategies for thriving.

## How I got here

I got into software engineering through the side door. After a short but thrilling career as a news photographer, I started my career at MojoTech, a software consultancy, as an apprentice, back before code schools were common. From there, I was promoted to "developer", no prefix. Another year later, I was promoted to "lead developer," which was more or less senior. There were no levels beyond that.

At my next job, a startup with a handful of engineers, I was hired as a senior and remained there for a year. We had no level beyond senior.

I left for another startup, where my title was also senior. Six months later, I was promoted to Lead Engineer. There were maybe two dozen engineers and as a Lead, I reported to the VP of engineering. I had one engineer who reported to me, so I was basically a tech lead manager.

I joined GitHub as a no-prefix "engineer", going down two levels. GitHub had a maybe ~300 engineers at the time. We had a total of eight engineering levels: Intern, 1/2/3, senior, Staff, Principal, and Distinguished. Our system remains more or less the same today with ~1,000 engineers.

My path to a staff role at GitHub started a couple of months into the job. I had the idea for ViewComponent and I pitched it to my manager Zaid, who gave me 20% time to pursue it. After a few months, I had a working prototype, which was the basis of my first presentation here at Boulder Ruby!

A year and a half after I joined, I was promoted to senior in large part due to the ViewComponent project. While at an all-company offsite, I pitched Diana, the leader of the design systems organization, on building out our design system in ViewComponent. A few months later, I asked to join her team to work on ViewComponent full time, which was granted.

As the summer of 2020 rolled around, there was a request for proposals for projects to address technical debt in our monolith, and I proposed having folks build and adopt ViewComponents for our design system to increase the consistency and quality of our user interfaces. I ended up leading a "virtual team" of about a dozen engineers for half the year, building and adopting ViewComponents.

The following spring, I was promoted to staff for this work. I've now been at staff for about five years.

## Defining the role

### Leveling

At many companies, the senior level is considered terminal, in that it's totally OK to never go beyond senior for your entire career. At least at our company, I've yet to hear about someone at senior being pressured to be promoted. The staff level is _beyond_ terminal. It's something you choose to pursue.

### Scope

In general, staff engineers work at a broader _scope_ than senior engineers, in breadth or depth.

While a senior engineer typically works at the team level, a staff engineer might work on problems that span multiple teams, potentially across different organizations. They might report to a director instead of a team-level manager, working across all of the director's teams.

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

Or, they go long. They might work on problems that take months or even years to solve, such as major product launches and migrations.

### Archetypes

Perhaps the best definition of the staff role is the archetypes from Will Larson's Staff Engineer: Tech Lead, Architect, Solver, Right Hand.

#### Tech lead

A Tech Lead "guides the approach and execution of a particular team. They partner closely with a single manager, but sometimes they partner with two or three managers within a focused area. Some companies also have a Tech Lead Manager role, which is similar to the Tech Lead archetype but exists on the engineering manager ladder and includes people management responsibilities." I've done this four times now at GitHub, each time covering for the absence of one of my Director's managers'. I've taken the Tech Lead Manager role, doing 1:1s with reports, serving as a hiring manager, and even helping with yearly reviews.

#### Architect

An Architect "is responsible for the direction, quality, and approach within a critical area. They combine in-depth knowledge of technical constraints, user needs, and organization level leadership."

Most of my work on ViewComponent at GitHub has fallen into this bucket, such as when I organized the effort to migrate to Primer ViewComponents.

#### Solver

A Solver "digs deep into arbitrarily complex problems and finds an appropriate path forward. Some focus on a given area for long periods. Others bounce from hotspot to hotspot as guided by organizational leadership."

My initial work on ViewComponent fell into this category. I worked with Aaron Patterson to develop a novel solution and wrote the upstream patch in Rails to make it work without a monkey patch.

#### Right Hand

A Right Hand "extends an executive’s attention, borrowing their scope and authority to operate particularly complex organizations. They provide additional leadership bandwidth to leaders of large-scale organizations."

This is a role I've fallen into a lot. For example, I wrote the initial draft of my director's quarterly/semester/yearly/multi-year plans, surfacing ideas proposed by IC engineers in our organization. I also worked on proposals for opening new engineering roles, hiring contractors, and worked with third-party vendors to evaluate potential new tools and services.

---

So you get more scope, working in the four archetypes. Sounds pretty fun, right? I think so. Now here are some ways I've found to thrive in the role.

## Strategies for thriving

### Align with archetypes

I like to use the archetypes to align with my manager to make sure our expectations are the same for a given project. I think this is useful at all levels, really. We should be regularly validating that our manager agrees with how we think about our work.

Something I've struggled with is seeing other staff engineers do impressive things in other archetypes and feeling like an imposter for not being like them. This is nearly always the case, as there is rarely a business need for two staff engineers that do the same thing. Continuously checking in with my manager on what I'm working on helps me overcome this worry.

It also speaks to a conundrum I've seen many seniors looking for promotion struggle with: there has to be a business need for a staff role. So if you're on a team with other staff engineers, it's generally harder than if no one else is staff. I'll be the first to admit that it was to my advantage to be the first staff engineer under my promoting director. This can feel unfair, and it is! At some point, you need to do staff-level work to be promoted to staff. There might not be any in your area, or even your company! Your manager should help you determine where staff opportunities might be, but it doesn't hurt to ask around either.

### Keep a public journal

A couple of years ago I adapted Julia Evans' [brag doc](https://jvns.ca/blog/brag-documents/) idea into a daily, internally-visible journal of what I worked on and what I listened to/read/watched. I was first motivated to do this to keep a record for self-reviews, but I quickly found that it was a helpful tool for guiding my focus towards things _worth writing down_, a.k.a. impactful work! I've also gotten feedback that it has helped others in the organizations I work in understand my role.

### Predict the future

Part of having impact at a breadth and depth beyond senior is looking towards the future. What are the internal trends (technical and non-technical) that could affect our part of the company? What about external trends? Are there new technologies we should experiment with? What is our competition doing technically that could make our customers want to use their product?

To avoid drinking from the firehose that is Twitter/Bluesky/Hacker News, I subscribe to the Hacker Newsletter, Ruby Weekly, and other topic-specific newsletters (such as accessibility news). This was especially important when working on accessibility as the legal landscape is constantly evolving in that area. Successful staff engineers are often cited by colleagues as sources of knowledge. This even comes up in interviews: we look for staff engineer candidates to teach us something new during technical interviews.

### Check and balance

As an IC, I've often had moments where I felt like leadership didn't care enough about what I cared about, whether it was code quality, tech debt, or software craftsmanship. I see part of our job as staff engineers as representing the technical concerns of the engineering discipline to people in power outside of engineering. To be a check and balance on the product discipline by surfacing and justifying engineering-driven priorities. How to do this depends greatly on the situation, but using data is a way of creating a shared understanding of a problem.

Sometimes this is literally what you are assigned to do. I find myself being asked to weigh in on things a lot, often to settle a disagreement. It can be a risky proposition. You don't want to parachute in and act like you know it all.

### Disambiguate, then delegate

I believe that a good staff engineer is continuously looking to downgrade the level of ambiguity in their work, with the goal of handing it off to someone else. Any time I'm handed a new problem, I ask myself: what will it take to have a senior or even a whole team work on this? Often, it comes through creating proofs of concept, reading papers, trying new technologies, and connecting with industry peers to validate the right solution to an ambiguous problem.

For example, my colleague Jon was tasked with finding a replacement for our usage of Styled Components. He looked to see what others in the industry were doing, tried some new technologies (CSS Layers), and did several proofs of concept before leading a team of a half dozen engineers to make the migration to CSS Modules.

### Generate energy

We expect staff engineers to be a source of creative energy. Succeeding in such a large scope of impact is very difficult if you can't inspire others to join you on your quest. For example, when I was working on migrating our monolith to ViewComponent, a good chunk of my daily responsibilities were around motivating others, whether through pairing, hosting office hours, or writing case studies of our work's impact.

### Create clarity

For example, I was given the ambiguous task of defining our strategy for prioritizing which parts of our application to audit and remediate first. I used our data warehouse to produce a report showing the distribution of traffic across our 2,000+ pages, highlighting which pages were used by the average user in a given week. We identified a few dozen product areas and prioritized working with those teams.

More generally, this can mean being the person in meetings who pushes for clear definitions of problems, proposed solutions, and success criteria.

### Deliver success

We lean on staff engineers to come through when we need it most. Whether something has to ship on time, a critical project is stalled, or a service is failing SLA in a novel way, we rely on staff engineers to solve our trickiest problems. This pressure is not for everyone! I've only had a couple projects like this in my time here, but they have all been a thrill.

For Jon, examples of critical projects include migrating all of GitHub.com to be responsive and implementing dark mode, all with minimal regressions. Delivering success is the path to being promoted to staff. Do enough impactful things, and at some point you become so senior that it's unfair for new seniors to have the same title.

## Conclusion

So that's how I got to staff, how I define the role, and some tricks for thriving in it.

Ultimately, the staff role is not for everyone. It's a very different job from being a senior engineer.

If you're interested but not sure, it might be worth asking your manager for an opportunity to try out one of the archetypes for a project. Maybe they need someone to cover for paternity leave, a temporary tech lead, or have an interesting area of research.

For me, it was definitely the right decision to go for the promotion. I have thrived in the ambiguity of the role and really appreciate the flexibility it's given me to take a lot of different paths over the years.
