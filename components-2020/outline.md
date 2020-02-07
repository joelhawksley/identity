TITLE
Encapsulating Views

ABSTRACT
Unlike models and controllers, Rails views are not encapsulated. This makes them hard to reason about and difficult to test, leading us to use abstractions such as presenters and decorators. In this talk, we'll explore the inner workings of how Rails compiles and executes views today, and the lessons we've learned building encapsulated views at GitHub over the past year.

DETAILS
This talk is given in story form.

In introducing the talk, I will highlight how Rails is built through extractions from existing applications.

I introduce the topic of the talk by discussing an extraction I couldn't ignore, telling the story of how I have seen a pattern of Rails applications turning to decorators, presenters, react components, and logic-filled partials as they scale. These abstractions are basically boilerplate at this point, and if there’s one thing we like about Rails it is that it eliminates boilerplate.

Then, I tell the story of how others have encountered these patterns in their applications, using survey data I gathered from my local Ruby community.

Next, I explore why Rails developers turn to these abstractions: testing. Rails views are difficult to test, and it's because they aren't encapsulated, a key construct and benefit of object-oriented design.

After a brief explanation of encapsulation and how it manifests itself in Rails, giving examples of models and controllers, I tell a detailed, technical story of the Rails render call stack, showing the internals of how Rails views are compiled into methods on a single global object, demonstrating how it's possible to share instance variable state in between views.

Then, I discuss the implications of this architecture, explaining how it makes testing difficult and can lead to performance issues at scale.

In contrast, I demonstrate how ViewComponent compiles views onto one object per view, providing proper encapsulation, as a superset of the Rails view architecture. I explain how this helps Rails views better follow the single responsibility principle.

Next, I highlight some features built by members of the community, including generators, component previews, and multiple content areas.

Finally, I share how we see components fitting into the architecture of a typical Rails application, and how we've migrated existing views and view models to components. I highlight benefits of migration that we’ve seen, such as improvements in test coverage.

I end the talk by revisiting the theme of Rails being built by extractions, and encouraging the audience to consider what they can contribute to Rails.

PITCH
I am the creator and maintainer of ViewComponent. This talk builds on a talk I gave at RailsConf last year, incorporating what we've learned building and using ViewComponent for the past year at GitHub and providing a technical argument for the architecture. This talk will be much more of a deep dive into Rails internals. While my talk last year was theoretical and worked with a prototype, this one is practical and discusses implementation in depth as well as real world implications and benefits. The video of last year's talk was one of the most viewed from the conference, indicating strong community interest in the topic.