Intro
  When I first joined GitHub, I was blown away by how we used linters. It was unlike anything I had seen in any other Ruby codebase before.
  There seemed to be a linter for everything you could think of. There were linters for things I never thought could be linted. For someone who likes linters, it was like walking into some sort of alternative universe.
  Since then, I've helped onboard other engineers who have also been take aback by our linters. It's made me think that it might be worth sharing our approach with the world.
  My goal today is to share that sense of wonder with all of you.
Hi
  But first, hi!
  My name is Joel
  I live just outside of Boulder, CO. Here is the required picture of me and my best friend Captain
  I'm an engineer on the design infrastructure team at GitHub.
  Our team builds the tools GitHub developers use to build user interfaces across platforms.
Intro 2
  But back to it. Let's talk about linters.
  Today I'm going to share how we use linters at GitHub
    I'll talk about why we use linters
    I'll give a ton of examples of the different kinds of linters we use
    and I'll share some things we've learned along the way
  But first, a disclaimer
  This isn't meant to be an example of what to do, or not to do
  What we do at GitHub might not make sense in other codebases
  But rather a window into the realities of how our linters work today
Today
  But first let's talk about today.
  After over 14 years and a million commits, GitHub remains a monolithic application
  Albeit perhaps more of a citadel
  We have a few dozen services
  But we serve our customer-facing traffic through Ruby.
  And it's a lot of Ruby.
  We have something approaching 2 million lines of Ruby code
  And perhaps more importantly, we have over a thousand engineers contributing to that single Ruby codebase.
  So that's a bit about where I'm coming from
Why
  That scale is the primary driver for our usage of linters.
  Define what a linter is
    Automated feedback on code
  Good feedback
    One thing that stuck out for me as I did this survey is how much it is a reflection of what makes feedback good in general. It comes down to three common criteria:
      Specific Timely Actionable
      Our team is responsible for setting lots of rules and guidelines. We want to help people succeed at building UIs that are up to our standards. We don’t want to be the police. We want to provide feedback that is helpful actionable etc
Examples
  Linters as tests
    We write code with assertions about the static state of our codebase
    Around a three hundred of these
    Regex linters (like a find and replace)
      AllowDeny language: fast/linting/allow_deny_language_test.rb
      Profanity test: fast/linting/profanity_test.rb
      Migrating deprecated patterns
        test/fast/linting/deprecated_boxed_group_usage_test.rb
    Global counters for patterns we want to avoid
      we have a few dozen of these
      test/fast/linting/html_safe_test.rb
      we use this kind of test to ensure that the right team is pinged to review a change
      this approach can quickly lead to merge conflicts if the count changes a lot
      it has been especially painful when multiple people deploy one PR after another that touches the counter
      So when we ran into this, and migrated to file name registry: https://github.com/github/github/pull/178978
    Tracking additions to files
      Similarly, we have a linter for flagging changes to files we don't want people to edit
      test/fast/linting/hacks_are_frozen_test.rb
    Code-deletion process
      Styles match markup test/fast/linting/styles_match_markup_test.rb
      Unused templates test/fast/linting/unused_templates_test.rb
    Upside: specific (and actionable)
    Downside: but not timely (often encountered on PR, which is late to the gam)
  Custom ERBlinters
    About two dozen
    Auditing written copy to ensure it matches our style guide, using ERBLint
      Even in this most simple, primitive form, we can see how linters can help elevate the conversations we have on our code reviews. I now don't need to leave a comment on capitalizing the H in GitHub, which means that I can focus on more important things in my review.
    No redundant alt tag: .erb-linters/accessibility/a11y_no_redundant_image_alt.rb
      Helps guide developers to follow accessibility guidelines
      We're asked to do so much as full stack developers
      Our ability to do as much as we do comes from the power of abstractions to simplify complex things
      This is an area my team is working a lot on as we focus on making GitHub more accessible
      Our team is small relative to the rest of the company
      But we're able to leverage linters to drive organizational change in a way we never could otherwise.
    tooltip counter .erb-linters/tooltip_counter.rb
      helpful message (actionable)
      autocorrecter adds exception
  Custom Rubocops
    Rubocop was the first linter we added
      Colleague Jon found the PR where he introduced it back in 2014 alongside SCSS lint
      The company had grown to around 150 people and there were no linters at all! There really wasn't a particular event that prompted adding rubocop, but people were using different styles of formatting that made the codebase inconsistent.
      And he established a practice we still use today: fix first, lint second.
      When he introduced Rubocop, he only turned on rules that passed.
      Then, he turned on rules one at a time, committing the necessary fixes before enabling enforcement in CI.
      We still use this technique today! And it has some nice benefits. By making the changes before introducing the automated enforcement, we're able to confirm that we in fact want to enforce the rule at all!
        https://github.com/github/github/pull/23539
        https://github.com/github/github/issues/23397
      https://github.com/github/github/pull/186008
    Every time I leave a comment on a PR, I'm wondering about whether I can automate it
      Because I can't be sure that I'll be the one reviewing the next PR that might make the same error
      Or honestly, that that I reliably catch a given error 100% of the time I review code
      Or perhaps I just want to take a vacation!
    Examples
      We have around 125 custom rubocops
      Don't branch on environment: github/do_not_branch_on_rails_env.rb
      AST-driven auto-correction
        PVC example? linters as part of deprecation lifecyle
        In-editor feedback (timely)
    Fanning out large refactors to other teams with Areas of Responsibility and Error Budgets
    But it's tricky to write custom rubocops
      I still struggle with nodepatterns
      And really feel like we're missing a simpler abstraction on top of them. I think a lot more people would write custom rubocops if nodepatterns were easier to work with.
    Extracting linters to gems for use across repositories
      https://github.com/github/rubocop-github
      PVC built-in linters
  Non-blocking linters that "nudge" engineers towards best practices
    We have a GitHub app called sentinel
    About a hundred rules
    Originally meant for providing automated application security reviews
    Regex powered
    Leaves comments on lines of PRs
    Non-blocking, which is nice for cases we can't be 100% confident
    For example, HTML comments https://github.com/github/sentinel/blob/master/config/rulesets/dotcom.yaml#L399
    Allows us to have a form of per-line ownership of files, kind of like codeowners
    for example: https://github.com/github/sentinel/blob/master/config/rulesets/dotcom.yaml#L154
  Using reporting tools like Datadog to track technical debt
Conclusion
  We use linters to:
    ensure our practices are applied consistently.
    shorten the feedback loop of the development process.
    give us room to provide higher value code reviews. Automation gives us space to focus on more nuanced concerns
  Good feedback
    One thing that stuck out for me as I did this survey is how much it is a reflection of what makes feedback good in general. It comes down to three things:
      Specific Timely Actionable
      Our team is responsible for setting lots of rules and guidelines. We want to help people succeed at building UIs that are up to our standards. We don’t want to be the police. We want to provide feedback that is helpful actionable etc
  But taking a step back
    But at what cost?
    To what end?
    Writing this talk has given me time to think about why we have linters in the first place.
    The best code is no code
    The best feedback is feedback you don't have to make
    Even as a linter
    In a lot of cases, we are linting for safety
    Most of the ruby today isn't typed
    It's also very dynamic
    It's not compiled
    Yet our analysis is static
    I can't help but feel a similar tension to what I notice when switching between dynamic, statically typed, and compiled languages.
    Linters shouldn't be the end of the road. How can we build systems that are correct and compliant by design?

To-do

mike mcquaid use graphic from https://github.com/github/friction/issues/86?
call out the work of various hubbers
modify talk title, intro note about location depending on audience

Parking lot
  Domain boundary enforcement with Packwerk
  Intelligent code analysis with CodeQL