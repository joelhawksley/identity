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

OPEN QUESTIONS

Abstract - tell story of extracting code from GitHub to share with community and eventually Rails - convention helps us collaborate

tie back into encapsulation points after deep dive