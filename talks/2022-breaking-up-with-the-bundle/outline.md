Intro
  We have some lofty goals ahead of us at GitHub
  We want GitHub to look and interact differently
  It’s a liability to maintain over time. As design and engineering standards change over time, it’s difficult to update.
  If you make a change and don't know if it broke something, it will break you, eventually. It keeps me up at night
  The cost of changing 4500 views - confidence
  Pit of failure
  CI never fails for bad design - Visual regressions hard to detect
  Fragility vs. confidence
  So how do we climb out of the pit?
  I'm going to share mostly things that didn't work

  CSS Still Sucks - Greg Raiz who even wants the cascade? If we got rid of it things would be better
  append only CSS
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

What
  What worked and what didn't as we've taken on the bundle
  How we've communicated our priorities to management
    I had a bad spider sense about our technical debt. That’s not enough to convince others to help, let alone my manager to give me and others time to work on it. We needed a plan.
    My hunch was twofold: we had a lot of technical debt and it was continuing to increase with remediation.

Measurement
  Did this far too late in the process
  Error budget. How to measure anything
  Custom CSS as measure of system's effectiveness
  Datadog dashboard
  Graphs used by leadership to plan work
    communicating evergreen needs

Things we tried
  Linting
  Color modes cleanups
  Bundle splitting / Kris Jan epic
    https://github.com/github/design-infrastructure/issues/1311
  Sidecar CSS
    CSS in JS experiment - broccolini tweet
    CSS modules ruby experiment
    Failure to inspect output buffer
      Caching
        octicon usage - feature flag caching bug
        critical css
      how rails templates work
        what about in python, java, react
    Declarative shadow DOM with template tag works with JS disabled
    Can use ViewComponents, or just partials
  CDP CSS diffing
  Extracting components
    Maturity lifecycle
    Axe previews etc
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
  At our scale there are fewer easy problems. Stack overflow becomes less useful. Rails gives us fewer tools. It's lonely.
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