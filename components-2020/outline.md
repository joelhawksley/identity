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
    Secret to share
    The future of Rails
    Is inside the applications and gems you're working on right now
    Will you set it free?

^ Lots of pauses in hook/intro/thankfulness

Bio intro
    Name
    Work at ~Microsoft~ GitHub
        ![100%](img/github.png)
        Distributed
        Pajamas joke
        Human contact - picture of captain
    Current passions
        digital wellness
        epaper

Thankfulness
    "No person hands out their money to passersby, but to how many do each of us hand out our lives!"
    "We’re tight-fisted with property and money, yet think too little of wasting time, the one thing about which we should all be the toughest misers."
    — SENECA, ON THE BREVITY OF LIFE, 3.1–2
    - https://zenchongproject.wordpress.com/2019/12/09/meditation-on-mortality-december-9th-spendthrifts-of-time/

    For your time
    For community
        meetup is well over a decade old
        some of us have been writing ruby for a long
        friends -> family
    For rails
    For ruby

Business value of Rails
    Best named codebase
    GitHub scale details
    GitHub is pretty Railsy
    Focus on value for our orgs, delivering value

Rails is an extraction - what can you extract?
    Eileen quote about upstream by default
        When I joined GitHub, I remember something @eileencodes said early on: If it doesn't have to do with our business, it needs to go in Rails.
        In other words, our mindset was to be "upstream by default"
        Why do we do this?
        We didn't always work with stock Rails.
        In fact, up until 2018, we were on long running forks of both Rails and Ruby.
        The maintenance burden of this arrangement grew over time to be unsustainable.
        reference her Talk about the future of rails at github etc
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
    Views have felt like they are missing something
    You all have seen this in your own apps
        it's pretty clear that a lot of us are dealing with this
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