Intro
  We have some lofty goals ahead of us at GitHub
  We want GitHub to look and interact differently

  This talk is as much about what not to do

  Global variables are bad, don’t hold CSS to standards we use for other code
  hard to split up CSS and serve only what is needed
  bundle cache broken by many deploys
  I see all the cool kids having fun on the React playground and I'm jealous
  And I joined them! It was fun. Kind of
  CSS is easy to delete in react
  But it wasn’t the same. No one could agree on anything. More time spent on tools than serving customers. I missed that about rails
    React is great but we can't rewrite everything
    Almost all of GitHub is still ERB
    Theme: continue to adopt ideas from react ecosystem, that's what VC is
  Each design permutation is effectively writing a new method that behaves subtly differently from an existing one - avatars and icons are context dependent
  Components are about correctness. What does it say about our work that we need to take and compare screenshots
    It means a lack of confidence

Measurement
  Error budget. How to measure anything
  Linting / color modes cleanups to assign team ownership

Things we tried
  CDP CSS diffing
  Extracting components
    Maturity lifecycle
    Axe previews etc
    cleaning up custom CSS manually is very risky and time consuming
    Implement rules from system in rails
      Button group buttons must all be same size
      Tobias marketing example - props as data vs. children
        https://github.slack.com/archives/D01JNV3SSS2/p1635407465000700
    components are extracted, not built
    autocorrection migration
      https://github.com/primer/view_components/pull/625

Big picture
  If you dig deep enough, most problems are human, not technical
  Design systems are more than CSS. They are structure, accessibility,
    Examples without complexity make it difficult to assess potential solutions. TODO apps don't expose the complexity of our scale

  There are a lot of potential solutions. It might need more than one solution. A system of solutions.

  We can’t expect everyone to be experts in all parts of the stack. We can't all be CSS and HTML experts, same with AR and SQL

  Code that is used once is high cost, low value

  Don't have to follow the crowd
    ideas should not be conflated with technologies
    ideas can work across languages and frameworks
    What do you like about X?
      because it's X?
      not because it does y and z
      storybook is a good example
    Good artists copy, great artists steal