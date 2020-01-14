2020 Conference Proposal

# Title
Views, Encapsulated
Encapsulating Views
ActionView::Component - The Missing Abstraction
The Missing Abstraction

# Format
Session

# Track
Rails at Scale
General

# Abstract
Unlike models and controllers, Rails views are not encapsulated. This makes them difficult to test and tricky to reuse, leading us to use abstractions such as presenters and decorators. In this talk we'll explore the lessons we've learned at GitHub building and using ActionView::Component over the past year.

# Details

This talk is given in story form.

In introducing the talk, I highlight how Rails is built through extractions from existing applications. 

I introduce the topic of the talk by discussing an extraction I couldn't ignore, telling the story of how I have encountered decorators, presenters, react components, and logic-filled partials in Rails applications throughout my career.

Then, it tells the story of how others have encountered these patterns in their applications, using survey data I gathered from my local Ruby community. 

Next, it explores why Rails developers turn to these abstractions: testing. Rails views are difficult to test, and it's because they aren't encapsulated, a key construct and benefit of object-oriented design.

After a brief explanation of encapsulation and how it manifests itself in Rails, I tell a detailed story of the Rails render call stack, showing how Rails views are compiled into methods on a single global object, demonstrating why it's possible to share instance variable state in between views.

Then, I discuss the implications of this architecture, introducing the idea of compiling views onto individual objects instead of a single global object, and how this enables unit testing of views.

Next, I highlight some features built by members of the community, including generators, component previews, and multiple content areas.

Finally, I share how we see components fitting into the architecture of a typical Rails application, and how we've migrated existing views and view models to components.

I end the talk by revisiting the theme of Rails being built by extractions, encouraging the audience to consider what they can contribute to Rails.

# Pitch
I am the creator and lead developer of ActionView::Component. This talk builds on a talk I gave at RailsConf last year, incorporating what we've learned building and using ActionView::Component for the past year at GitHub. My talk from last year was the third-most viewed on YouTube from the conference, including the keynotes, indicating strong community interest in the topic.

# Name
Joel Hawksley

# Bio
Joel is a software engineer at GitHub. He works on the Design Systems team, creating tools to enable the development of consistent, high-quality user interfaces.

Details
  Take-aways
  Refactorings?