TITLE
The Missing Extraction

ABSTRACT
Rails is missing an extraction, and it's hiding in plain sight, right inside your application. 

After itself being extracted from Basecamp, Rails has remained relevant for over a decade because others have contributed pieces of their applications into the framework. If Rails is going to survive another decade, it will need you to contribute your extractions too. 

In this talk we'll extract ActionView::Component from the GitHub monolith for upstreaming into Rails (with a deep dive into the Rails view layer along the way), showing how Rails can evolve through extractions from existing applications.

DETAILS
The goal of this talk is to inspire the audience to think about how they can contribute to Rails, to educate them on how the Rails view layer works today, and to explore an extraction from the GitHub monolith into Rails.

As our applications evolve over time, we often turn to tools outside of Rails to manage the complexity of our views, such as decorators, presenters and view models. At GitHub, we’ve incorporated ideas from these patterns into ActionView::Component. In this talk we’ll explore the patterns ActionView::Component introduces and share the lessons we’ve learned using it in production at GitHub over the past year and a half.

I'll demonstrate this by implementing a component from our design system with helpers, a decorator, a presenter, a view model, and even react-rails, highlighting the tradeoffs of each approach. It will then show how implementing it as an ActionView::Component is influenced by each of the previous approaches.

I'll also cover how we’ve migrated existing views to this architecture, leveraging some of the unique features of ActionView::Component, such as ActionView::Component::Preview and stateless components.

This talk is at the beginner to intermediate level. 

PITCH
I'm a software engineer at GitHub, working on one of the largest, most-trafficked Ruby on Rails applications in the world. Over the past year, I've lead the development of ActionView::Component, both at GitHub and with the open-source community. My talk on the initial prototype of ActionView::Component was the third-most popular of RailsConf 2019 based on YouTube views.

GOALS
- Inspire audience to think about how they can contribute to Rails
- Educate audience on how the Rails view layer works today
- Create a moment of presence, clarity, and vulnerability
- Exemplify GitHub's commitment to doing work that benefits the Rails community

STRUCTURE

Hook
    Rails has been around for a long time. Practically an eternity in internet time. The internet has changed, and somehow Rails has managed to stay relevant. 

    But this hasn’t been by accident. Rails isn’t carved in stone. It’s evolved over time. And it’s evolved because people like us have made it better by contributing new features and fixing bugs.

    Today I’m going to talk about a new way of building views, called ActionView::Component. 

    My goal is to share an understanding of why we built it, what we’ve learned so far in using it for the past year, and maybe inspire you to give it a try yourself.

Bio intro
    Current passions
        digital wellness
        epaper

Thankfulness
    For community
        Sponsors 
            Food
            Meeting space
            Sandi Metz
        Dan, Rylan, Marty
            meetup is well over a decade old
            some of us have been writing ruby for a long
        You
            You make it special
            You make this community feel like family
        Something special here
        Prakash
    For your time
        "No person hands out their money to passersby, but to how many do each of us hand out our lives!"
        "We’re tight-fisted with property and money, yet think too little of wasting time, the one thing about which we should all be the toughest misers."
        — SENECA, ON THE BREVITY OF LIFE, 3.1–2
        - https://zenchongproject.wordpress.com/2019/12/09/meditation-on-mortality-december-9th-spendthrifts-of-time/
        I’ve put a lot of time and energy into this talk with the intention to make it worth your time.
        So before we begin, I have a simple request: 
        Be present. There are many hours in the day to use our phones, to check Slack and email. I’d love to share this next half an hour or so with all of you in the present moment, not somewhere else.

    For rails
        Rails has been around a long time. How long have you been using it? Think about how much money you’ve made writing rails code. Think about how much value rails has brought to the companies you’ve worked for.  
    For ruby

Business value of Rails
    Best named codebase - github/github/github
    GitHub scale details
        We’re still largely a Rails monolith. In fact, we’ve recently been moving some of our services *back* into the monolith.

        We have X models, X controller, and X views.

        Our codebase is about twelve years old. It’s only about three years younger than Rails!
    GitHub is pretty Railsy - Our app is more boring than you’d think
    Focus on value for our orgs, delivering value

Rails is an extraction - what can you extract?
    DHH said something similar back in 2007: 

    “The best frameworks are in my opinion extracted, not envisioned. And the best way to extract is first to actually do.”
    https://dhh.dk/posts/6-why-theres-no-rails-inc.html

    Eileen quote about upstream by default
        When I joined GitHub, I remember something @eileencodes said early on: If it doesn't have to do with our business, it needs to go in Rails.
        In other words, our mindset was to be "upstream by default"
        Why do we do this?
        We didn't always work with stock Rails.
        In fact, up until 2018, we were on long running forks of both Rails and Ruby.
        The maintenance burden of this arrangement grew over time to be unsustainable.
        reference her Talk about the future of rails at github etc
        We had to constantly back port security fixes.

        It was hard for new engineers to get up to speed on Rails, GitHub Edition.

        Over the course of almost two years, Eileen and a team of several dedicated engineers managed to get us back to Rails master.

        This was an incredible accomplishment.

        Among the many benefits, it enabled us to contribute to Rails again.
    Backpack analogy
        "frameworks are extracted, not built"
        decisions you don't have to make

Problem intro - story
    "An extraction that became too obvious for me to ignore any longer"
    Teespring / decorators
    Galvanize / react - rails - isolation & testing
    GitHub / presenters 
    trend towards components / design systems
        need for consistent use of CSS + correct HTML

Problem statement
    Server-rendered views in Rails are pretty great. They’ve gotten us this far. But I’m sure many of you have felt their shortcomings.

    When I asked you all to share screenshots of your Rails app folders, I was looking for something.

    First of all, thank you for sharing this little window into your applications.

    Let’s look at them and see.

    There’s a lot of view-related abstractions. 

    Presenters

    Decorators

    View models

    Conservatively, way more than half of you had one of these in your codebases. And none of these are provided by Rails itself!

    Now I’m going to go out on a limb and guess that none of your companies are in the business of view layer innovation.
    Views have felt like they are missing something
    You all have seen this in your own apps
        it's pretty clear that a lot of us are dealing with this
    So why do we find ourselves straying from the tools Rails gives us to build our views?
    why aren't views easy to test?
        testing pyramid
        encapsulation diagram
    "testing and encapsulation"
    cells gem
    drape and cells have millions of downloads
    Every Rails app I've worked in has done something similar
    Whether using these gems or rolling something custom.
    actionview precompiler gem from jhawthorn
    all variants of view
    render full path linter rule
    Server rendered views aren’t going anywhere
    We have almost 4000

Deep dive into rails views
    instance variables work in between views as question
    answer via deep dive
    Single module
    List number of methods defined dynamically on GH app
    Why this is bad
    encapsulation

Our solution
    existing hundreds of view models
    idea while traveling
    Set out to collect these ideas and think about what it might look like to bring them into Rails
    boulder ruby talk
    rails talk
    rails PR 
    gem
    OS contributions
    struggles - losing confidence regularly
    regular pairing
    What we do is the best:
    Encapsulating into a single object
    Easier to make fast
    Better than partials and helpers
    Instance variable context encapsulation
    superset of the rails view layer
    Works exactly as you’d expect it to
    peformance
        Requests per second
        It works for us
    rails patches
        In June, we landed a patch in Rails that added support for `render_in`
        Support from Rafael
    gem
        In August, we published version one of the `actionview-component` gem, extracting the library from `github/github`
        Since then, we've shipped X releases
            With a large majority of contributions coming from the Rails community
        Blown away by support
            contirbutors slide
        My first open source project
        We've added a bunch of features
            Generators - kasper
            Previews - juan manuel ramllo
    Migration path
        “If it could be a partial, it could be a good component”
        View models
        Migrate controller tests

Case study
    Dave ramsey examples


Extraction example
    class_names helper from react
    bugs 
    bad docs

Conclusion
    Rails has a lot of room to grow
    The future of Rails is inside your applications, right now
    The world will keep changing
    It's up to us to make thoughtful extractions to keep Rails relevant

OPEN QUESTIONS
Ask for feedback at the end of talk - what was confusing? What needs clarifying?
Abstract - tell story of extracting code from GitHub to share with community and eventually Rails - convention helps us collaborate
"Time is precious, how willyou spend yours?" I certainly don't want to spend mine re-inventing the wheel
Frameworks like Rails help us move human progress forward, allowing us to focus on new and important problems, not preventing CSRF forgery
Lots of pauses in hook/intro/thankfulness