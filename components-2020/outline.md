TITLE
The Missing Extraction

ABSTRACT
Rails is missing an extraction, and it's hiding in plain sight, right inside your application. 

Rails itself was extracted from Basecamp, and has remained relevant for over a decade due to many others upstreaming pieces of their applications into the framework. If Rails is going to survive another decade, it will need you to contribute your extractions too. In this talk we'll extract ActionView::Component from the GitHub monolith for upstreaming into Rails, taking a deep dive into the Rails view layer along the way, showing how Rails can evolve through extractions from existing applications.

DETAILS
Rails is missing an extraction: as our applications evolve over time, we often turn to tools outside of Rails to manage the complexity of our views, such as decorators, presenters and view models.

At GitHub, we’ve incorporated ideas from these patterns into ActionView::Component, which we plan to upstream into Rails. In this talk we’ll explore the new features ActionView::Component introduces and share the lessons we’ve learned using it in production at GitHub over the past year and a half.

This goal of this talk is to inspire the audience to think about how they can contribute to Rails, tp educate them on how the Rails view layer works today, and to explore an extraction from the GitHub monolith into Rails.

I’ll share some examples of components we’ve built at GitHub, including how we’ve migrated existing views to this architecture. I’ll also cover some of the unique features of ActionView::Component, such as ActionView::Component::Preview and stateless components.

This talk will take a simple UI example from the GitHub application and walk through implementing it with helpers, a decorator, a presenter, a view model, and even react-rails, highlighting the tradeoffs of each approach. It will then show how implementing it as an ActionView::Component is influenced by each of the previous approaches.

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
    Is inside the applications you're working on right now
Bio intro
    Name
    Work at ~Microsoft~ GitHub
    
Thankfulness

Business value of Rails
    Focus on value for our orgs

Rails is an extraction - what can you extract?
    Eileen quote about upstream by default
        reference her Talk about the future of rails at github etc

Problem statement
    Views have felt like they are missing something
    You all have seen this in your own apps
    why aren't views easy to test?
    actionview precompiler gem from jhawthorn
    all variants of view
    render full path linter rule

Deep dive into rails views
    instance variables work in between views as question
    answer via deep dive

Our solution
    existing hundreds of view models

    idea while traveling
    boulder ruby talk
    rails talk
    rails PR 
    gem
    OS contributions
    struggles
    regular pairing

OPEN QUESTIONS

What are the take-aways?

"Rails still has a lot of room to grow" 

"An extraction that became too obvious for me to ignore any longer"

Ask for feedback at the end of talk - what was confusing? What needs clarifying?