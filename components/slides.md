autoscale: true
theme: Simple, 1
text: Avenir Next Medium, #24292e
text-strong: Avenir Next Bold, #24292e
header: Avenir Next Medium, #24292e
header-strong: Avenir Next Bold, #24292e
code: Menlo Regular, #6f42c1, #005cc5, #0366d6, #d73a49, #d73a49
background-color: #ffffff;

# [fit] Rethinking the View Layer<br>with Components

^ Good morning everyone

---

# [fit] Joel Hawksley
# hawksley.org

^ Name is Joel

^ And I...

---

![40%](img/github.png)

^ work at GitHub

---

^ PAUSE

---

# [fit] Creativity

^ Creativity is the ability

---

# [fit] Imagine

^ to imagine something new.

^ It is not the ability to create

---

# [fit] Something

^ Something out of

---

# [fit] Nothing

^ Nothing, but to generate

---

# [fit] New ideas

^ New ideas by

---

# [fit] Combining

^ Combining,

---

# [fit] Changing

^ Changing,

---

# [fit] Reapplying

^ or reapplying

---

# [fit] Existing Ideas

^ existing ideas.

---

![50%](img/react.png)

^ Today we're going to do just that:

^ We're going to take ideas from React,

---

![50%](img/rails.png)

^ And reapply them in Rails.

^ In doing so, we we're going to take a template that

---

# [fit] Testing

^ is hard to test thoroughly

---

# [fit] Code<br>Coverage

^ is impossible to audit with code coverage tools

---

# [fit] Data Flow

^ makes it difficult to reason about data flow

---

# [fit] Standards

^ and fails basic Ruby code standards,

^ And refactor it into a new addition to Rails

---

# [fit] ActionView::Component

^ called ActionView::Component that

---

# [fit] Testing

^ is tested thoroughly in isolation

---

# [fit] Code<br>Coverage

^ is audited with code coverage tools

---

# [fit] Data Flow

^ only receives the data it needs

---

# [fit] Standards

^ follows the code standards of the Ruby language

---

# [fit] >200x

^ and over 200x faster to test

---

^ PAUSE

---

# [fit] Views

^ But first

^ What even is a view?

---

# [fit] Data → HTML

^ Views are functions

^ They input (data), and return HTML.

^ How has the Rails view layer evolved over the years?

---

[.header: alignment(left)]

# [fit] 2004 **ERB 1.0**
# [fit] 2005 **Rails 1.0**
# [fit] 2012 **Turbolinks**
# [fit] 2016 **API Mode**

^ It's been pretty stable!

^ Rails still ships with ERB like it did in 2005

^ Rails 4 added Turbolinks

^ And Rails 5 added API mode

---

^ PAUSE

^ But in the last couple of years, the winds have begun to change.

^ But I think it's telling that DHH said in the Rails 5 release notes:

---

# [fit] Rails is not only a great choice when you

^ Rails is not only a great choice when you

---

# [fit] want to build a full-stack application that uses

^ want to build a full-stack application that uses

---

# [fit] server-side rendering of HTML templates

^ server-side rendering of HTML templates,

---

# [fit] but also a great companion for the

^ but also a great companion for the

---

# [fit] new crop of client-side JavaScript or native applications

^ new crop of client-side JavaScript or native applications that

---

# [fit] just needs the backend to speak JSON.

^ just needs the backend to speak JSON.

---

[.header: alignment(left)]

# [fit] 2004 **ERB 1.0**
# [fit] 2005 **Rails 1.0**
# [fit] 2012 **Turbolinks**
# [fit] 2016 **API Mode**

^ The history of the Rails view layer is one of most of us moving away from it

---

^ So what does the view layer look like at GitHub?

---

# [fit] ERB

^ Still using embedded ruby

^ Why isn’t GitHub a single page app like everything else these days?

---

# [fit] Progressive<br>Enhancement

^ Progressive enhancement.

^ While javascript makes our user experience more pleasant, most of the app works without it.

---

# [fit] Why?

^ But why?

^ A couple reasons:

---

# [fit] Performance

^ While most of us here are lucky enough to be using modern, powerful devices

^ A lot of our new users are in developing countries

^ Low powered netbooks, chrome books, or tablets, which buckle under heavy Javascript.

---

# [fit] Browser<br>Support

^ Another reason is browser support.

^ Since we don't *need* javascript to run our site, we can simply turn it off for older browsers that are hard to develop for

^ which makes our javascript easier to maintain.

^ How do we do it?

---

[.code-highlight: all]
[.code-highlight: 3-6]
[.code-highlight: 2-6]
[.code-highlight: 8]
[.code-highlight: 3-6]
[.code-highlight: 2-6]
[.code-highlight: 8]

```erb
<% if supported_browser? %>
  <%= javascript_bundle 'polyfills' if compatibility_browser? %>
  <%= javascript_bundle 'frameworks' %>
  <%= javascript_bundle 'github', async: true %>
  <%= yield :scripts %>
  <%= controller_javascript_bundles %>
<% else %>
  <%= javascript_bundle 'unsupported' %>
<% end %>
```

^ Couple tiers of Javascript bundles

^ S Fully supported browsers -> normal bundles.

^ S Polyfills to second tier that need it.

^ S Unsupported -> ONLY smaller set of polyfills

^ So when we deprecate browsers, we move them through these

^ S three
^ S tiers
^ S of support

---

# [fit] Progressive<br>Enhancement

^ So what does progressive enhancement look like in practice?

---

![fit](img/pjax-1.png)

^ Take for example posting a new comment on an issue

^ JS intercepts click


---

![fit](img/pjax-2.png)

^ AJAX request returns DOM nodes for sidebar, comment form, timeline

^ Inject results into page

^ Using PJAX, like Turbolinks

^ Javascript turned off -> normal page request and reload

^ PAUSE

---

^ So what is it like to work on views at GitHub?

---

![fit](img/sticky.png)

^ I recently worked on adding sticky headers to pull request and issue pages.

---

![fit](img/issue-status-highlight.png)

^ As part of that project, I got to know this little piece of our UI, called the Issue Badge, really well.

^ We use the issue badge to display the status of issues and pull requests

---

![fit](img/primer.png)

^ It's part of our design system called Primer

^ Think of it as our own version of Bootstrap.

---

^ But before we dig into that let's talk about our data model.

---

```ruby
class Issue < ApplicationRecord
  belongs_to :pull_request
end

class PullRequest < ApplicationRecord
  has_one :issue, inverse_of: :pull_request
end
```

^ In the GitHub data model

^ Pull request is just an issue with an associated pull request object.

^ So all pull requests are issues, but not all issues are pull requests.

---

[.code-highlight: all]
[.code-highlight: 1, 5, 9, 13, 17, 21]
[.code-highlight: 3]
[.code-highlight: 2, 4]
[.code-highlight: 2-4]

```erb
<% if pull_request && pull_request.merged? %>
  <div class="State State--purple">
    <%= octicon('git-merge') %> Merged
  </div>
<% elsif pull_request && pull_request.closed? %>
  <div class="State State--red">
    <%= octicon('git-pull-request') %> Closed
  </div>
<% elsif pull_request && pull_request.draft? %>
  <div class="State">
  <%= octicon('git-pull-request') %> Draft
  </div>
<% elsif pull_request %>
  <div class="State State--green">
    <%= octicon('git-pull-request') %> Open
  </div>
<% elsif issue && issue.closed? %>
  <div class="State State--red">
    <%= octicon('issue-closed') %> Closed
  </div>
<% elsif issue %>
  <div class="State State--green">
    <%= octicon('issue-opened') %> Open
  </div>
<% end %>
```

^ We render the issue badge with this partial.

^ PAUSE

^ S Depending on the state of the pull request or issue, we:

^ S Render an icon, label,

^ S and color

^ S together displaying the state of issue or pull request

---

^ Wanting to know more about its behavior, I figured, why not just delete the file and see what tests fail!

^ That's just what I did.

^ And then I pushed to CI.

---

[.background-color: #28a745]
[.header: #ffffff]

^ The build was green.

---

^ How could this be?

^ You know, things are different at GitHub.

---

# [fit] Rails @ GitHub

^ GitHub is a Rails monolith that is just turned 11 years old.

---

# [fit] 209

^ Over 200 controllers, not including our API

---

# [fit] 556

^ We have over 550 models

---

# [fit] 3718

^ And over 3700 views!

---

^ So how might this scale affect our approach to testing our views?

---

# [fit] Testing

^ Right now, our main way of exercising our view code is through controller tests set up to render views.

---

# [fit] 6s

^ In our test suite, it takes six seconds to run a single controller test locally, not including setup.


---

# [fit] One Minute

^ That's one minute to run a set of ten cases.

^ I think we can agree that's far from ideal.

---

![50%](img/rails.png)

^ This problem is a symptom of several shortcomings in the Rails view layer.

---

# [fit] What trips you up with Rails views?

^ In a survey of my local ruby group, the number one response to this question was:

---

# [fit] Data Flow

^ Data flow.

^ A common data flow error we're probably all familiar with is

---

# [fit] N + 1

^ the good old N + 1, where we accidentally generate an expensive query in a view.

^ Our example code also has some data flow issues:

---

[.code-highlight: all]
[.code-highlight: 1, 5, 9, 13, 17, 21]

```erb
<% if pull_request && pull_request.merged? %>
  <div class="State State--purple">
    <%= octicon('git-merge') %> Merged
  </div>
<% elsif pull_request && pull_request.closed? %>
  <div class="State State--red">
    <%= octicon('git-pull-request') %> Closed
  </div>
<% elsif pull_request && pull_request.draft? %>
  <div class="State">
  <%= octicon('git-pull-request') %> Draft
  </div>
<% elsif pull_request %>
  <div class="State State--green">
    <%= octicon('git-pull-request') %> Open
  </div>
<% elsif issue && issue.closed? %>
  <div class="State State--red">
    <%= octicon('issue-closed') %> Closed
  </div>
<% elsif issue %>
  <div class="State State--green">
    <%= octicon('issue-opened') %> Open
  </div>
<% end %>
```

^ Looking at our example:

^ S For "pull request" and "issue", what attributes do we need from each object?

^ If these are active record objects, we’d be fetching their entire set of attributes, when we may in fact only need one or two for each object.

^ In addition, it's unclear where the "pull request" and "issue" variables are coming from, making it difficult to reuse this partial with confidence.

---

# [fit] Unit<br>Testing

^ Another problem is that unit testing views isn’t common practice in Rails

^ Rails encourages us to test our views through integration and system tests, which are expensive.

---

# [fit] Partials

^ This is especially painful for partials, as they

^ often end up being tested for each of the views they are included in

^ Leads to duplication of tests

^ Cheapens benefit of reusing the partial in the first place

---

# [fit] Code<br>Coverage

^ Another problem is measuring code coverage

---

# [fit] ~~SimpleCov<br>Coveralls~~

^ Neither SimpleCov nor Coveralls support view code

^ Combined with testing friction puts views in blind spot

---

# [fit] Implicit<br>Arguments

^ Another weakness is the lack of a method signature

^ Unlike a method declaration on an object, views do not declare the values they are expected to receive

---

[.code-highlight: all]
[.code-highlight: 1, 5, 9, 13]
[.code-highlight: 17, 21]
[.code-highlight: 1, 5, 9, 13, 17, 21]
[.code-highlight: none]
[.code-highlight: 1, 5, 9, 13, 17, 21]

```erb
<% if pull_request && pull_request.merged? %>
  <div class="State State--purple">
    <%= octicon('git-merge') %> Merged
  </div>
<% elsif pull_request && pull_request.closed? %>
  <div class="State State--red">
    <%= octicon('git-pull-request') %> Closed
  </div>
<% elsif pull_request && pull_request.draft? %>
  <div class="State">
  <%= octicon('git-pull-request') %> Draft
  </div>
<% elsif pull_request %>
  <div class="State State--green">
    <%= octicon('git-pull-request') %> Open
  </div>
<% elsif issue && issue.closed? %>
  <div class="State State--red">
    <%= octicon('issue-closed') %> Closed
  </div>
<% elsif issue %>
  <div class="State State--green">
    <%= octicon('issue-opened') %> Open
  </div>
<% end %>
```

^ Let’s go back to our example code.

^ What data does this view need to render?

^ S A pull request?

^ S An issue?

^ S Should I be able to pass in both?

^ S Neither?

^ S Are these values passed in as locals, or do they come from a helper?

---

# [fit] Standards

^ Our views regularly fail even the most basic standards of code quality we expect out of our Ruby classes.

^ Let’s go back to our example.

---

![fit](img/code-review.png)

^ If this was a method on a class, what aspects might we object to in a code review?

^ Besides it being a super long method, I can think of a couple:

---

![fit](img/code-review-1.png)

^ Where is octicon defined?

---

![fit](img/code-review-2.png)

^ Where does this class attribute value come from? This feels like a magic string.

---

![fit](img/code-review-3.png)

^ Where are pull_request and issue coming from?

---

# [fit] Standards

^ We regularly do things in our templates that we’d never do in a Ruby class

^ PAUSE

---

# [fit] Testing

^ So to recap,

^ Rails views are difficult to test

---

# [fit] Code<br>Coverage

^ and those tests are impossible to audit with code coverage tools, preventing us from knowing how thorough they are

---

# [fit] Data Flow

^ They make it difficult to reason about data flow

---

# [fit] Implicit<br>Arguments

^ Have implicit method signatures

---

# [fit] Standards

^ And often fail basic Ruby code standards

^ PAUSE

---

# [fit] MVC

^ These things make the Rails view layer

---

# [fit] MvC

^ more of a second-class citizen these days.

^ PAUSE

^ Given all of this, I don't think it's much of a surprise that a new way of building views has taken hold in the Rails community:

---

![50%](img/react.png)

^ React.

---

# [fit] Components

^ React is all about components.

^ A component is an object that encapsulates a piece of user interface.

---

[.code-highlight: all]
[.code-highlight: 2-4]
[.code-highlight: 7]
[.code-highlight: 3]

```jsx
class Greeting extends React.Component {
  render() {
    return <div>Hello, {this.props.name}!</div>;
  }
}

React.render(<Greeting name="World" />, document.getElementById('example'));
```

^ Here's one way of writing "Hello, World" in a React component.

^ PAUSE

^ React components, at a minimum,

^ S implement a render method that returns HTML.

^ S Arguments passed to a component are assigned to the `props` object,

^ S which is accessible within methods on the component.

---

[.code-highlight: all]
[.code-highlight: 5]
[.code-highlight: 4,6]

```jsx
class IssueBadge extends React.Component {
  render() {
    return (
      <div className={ "State " + this._stateClass() }>
        <i className={this._icon()} /> {this._label()}
      </div>
    )
  }

  _icon() { ... }
  _stateClass() { ... }
  _label() { ... }
}
```

^ Here’s an example of what the issue badge might look like as a React component.

^ S Like our template, the component renders an icon and a label

^ S Wrapped in a state-specific CSS class

---

# [fit] Types

^ Another dimension of the React architecture is types.

---

[.code-highlight: all]
[.code-highlight: 2-4]
[.code-highlight: 5,9]
[.code-highlight: 5-9]

```javascript
IssueBadge.propTypes = {
  issue: PropTypes.exact({
    isClosed: PropTypes.bool.isRequired
  }).isRequired,
  pullRequest: PropTypes.exact({
    isClosed: PropTypes.bool.isRequired,
    isMerged: PropTypes.bool.isRequired,
    isDraft: PropTypes.bool.isRequired
  }),
};
```

^ The Prop Types library allows React components to express some expectations about the data they receive.

^ In this case, we are expecting:

^ S An issue with the isClosed boolean to always be provided

^ S And a pull request to sometimes be provided, and if so,

^ S with the isClosed and isMerged, and isDraft booleans.

---

[.code-highlight: 10]

```jsx
class IssueBadge extends React.Component {
  render() {
    return (
      <div className={ "State " + this._stateClass() }>
        <i className={this._icon()} /> {this._label()}
      </div>
    )
  }

  _icon() { return this.props.issue.isClosed ... }
  _stateClass() { ... }
  _label() { ... }
}
```

^ This allows us to reference the isClosed boolean on issue without worry, as our type check will guarantee that it is present.

^ PAUSE

---

# [fit] Data Flow

^ Another advantage of React is how it simplifies data flow.

---

# [fit] Values > Objects

^ By passing values into views instead of rich objects, React encourages us to write functions without side-effects.

---

# [fit] Testing

^ Another cool thing about React is how easily components can be tested in isolation.

---

[.code-highlight: all]
[.code-highlight: 2]
[.code-highlight: 3]
[.code-highlight: all]

```jsx
it('should render the closed issue badge', function() {
  expect(shallow(<IssueBadge props={{ issue: { isClosed: true }}} />).
  contains(<div className="State State--red">Closed</div>)).toBe(true);
});
```

^ Here’s an example test that

^ S renders the component directly

^ S and then asserts against the output.

^ S What’s great is that this test runs without touching the database or controller layer.

^ Which means that really, really fast.

^ PAUSE

---

![50%](img/react.png)

^ So to recap,

^ React has:

---

# [fit] Components

^ Components that render HTML

---

# [fit] Types

^ Types that give us confidence in our inputs

---

# [fit] Data flow

^ Simplified data flow

---

# [fit] Testing

^ And lightweight testing in isolation

---

^ Which is too bad, because it’s not compatible with our progressive enhancement architecture.

^ But what if there was a way to incorporate some of the benefits

---

![50%](img/react.png)

^ of React

---

![50%](img/rails.png)

^ into Rails?

^ PAUSE

^ Before we start refactoring,

---

# [fit] Tests

^ Let's add some tests to make sure we don't break anything.

---

[.code-highlight: all]
[.code-highlight: 2-4]
[.code-highlight: 2]
[.code-highlight: 3]

```erb
<% if pull_request && pull_request.merged? %>
  <div class="State State--purple">
    <%= octicon('git-merge') %> Merged
  </div>
<% elsif pull_request && pull_request.closed? %>
  <div class="State State--red">
    <%= octicon('git-pull-request') %> Closed
  </div>
<% elsif pull_request && pull_request.draft? %>
  <div class="State">
  <%= octicon('git-pull-request') %> Draft
  </div>
<% elsif pull_request %>
  <div class="State State--green">
    <%= octicon('git-pull-request') %> Open
  </div>
<% elsif issue && issue.closed? %>
  <div class="State State--red">
    <%= octicon('issue-closed') %> Closed
  </div>
<% elsif issue %>
  <div class="State State--green">
    <%= octicon('issue-opened') %> Open
  </div>
<% end %>
```

^ What might it look like to test our view?

^ S In each case, we're doing three things:

^ S Setting a class name,

^ S icon, and label

---

[.code-highlight: all]
[.code-highlight: 1-9]
[.code-highlight: 6]
[.code-highlight: 7]
[.code-highlight: 8]

```ruby
it "renders the open issue badge" do
  create(:issue, :open)

  get :index

  assert_select(".State.State--green")
  assert_select(".octicon-issue-opened")
  assert_includes(response.body, "Open")
end

it "renders the closed issue badge"
it "renders the open pull request badge"
it "renders the closed pull request badge"
it "renders the merged pull request badge"
it "renders the draft pull request badge"
it "renders the closed pull request badge for a closed draft pull request"
```

^ To start, let's add some traditional controller tests for each state.

^ S We'll start with a test for the open issue badge.

^ We'll assert that we have the correct

^ S class name,

^ S icon,

^ S and label

---

[.background-color: #28a745]
[.header: #ffffff]

^ And now we have test coverage.

^ So let's delete the view and see what happens.

---

[.background-color: #d73a49]
[.header: #ffffff]

# [fit] 7 examples, 7 failures

^ We have failing tests!

^ Now we can refactor with confidence.

---

^ So what might a component look like in the Rails world?

---

```ruby
# app/components/issues/badge.rb

module Issues
  class Badge
  end
end
```

^ I think it would make sense to make it a class, like everything else in Ruby! Let's call it badge, inside the Issues module.

---

# [fit] API

^ And how might we call it in our view?

---

```erb
<%= render Issues::Badge, issue: issue, pull_request: issue.pull_request %>
```

^ The Rails way would be to use the existing `render` syntax.

^ So let’s see if we can get our first test to pass.

---

[.code-highlight: 3-9]

```ruby
module Issues
  class Badge
    def html
      <<-erb
      <div class="State State--green">
        #{octicon('issue-opened')} Open
      </div>
      erb
    end
  end
end
```

^ Let's add a method to our component that returns the open issue badge from our partial.

^ And then run our test.

---

[.background-color: #d73a49]
[.header: #ffffff]

# [fit] 'Issues::Badge' is not an<br>ActiveModel-compatible object.

^ Interesting. It looks like ActionView#render doesn't like being passed our component.

^ So let's teach it how to handle it!

^ Short of forking Rails and changing the original definition of ActionView#render

---

[.code-highlight: all]
[.code-highlight: 3-7]
[.code-highlight: 4]
[.code-highlight: 6]

```ruby
class ActionView::Base
  module RenderMonkeyPatch
    def render(component, *_args)
      return super unless component == Issues::Badge

      component.new.html
    end
  end

  prepend RenderMonkeyPatch
end
```

^ let's write a monkey patch!

^ S we'll re-define #render,

^ S So that when we pass in our component,

^ S it calls our component's #html method

^ So let's run our test again.

---

[.background-color: #d73a49]
[.header: #ffffff]

# [fit] undefined method 'octicon'

^ Undefined method octicon? That's interesting.

---

![fit](img/code-review-1.png)

^ Remember our code review comment about not knowing where the octicon method came from?

^ Now our code is asking us the same question!

---

```ruby
module Issues
  class Badge
    def html
      <<-erb
      <div class="State State--green">
        #{octicon('issue-opened')} Open
      </div>
      erb
    end
  end
end
```

^ Back in our component,

---

[.code-highlight: 3]

```ruby
module Issues
  class Badge
    include OcticonsHelper

    def html
      <<-erb
      <div class="State State--green">
        #{octicon('issue-opened')} Open
      </div>
      erb
    end
  end
end
```

^ let's tell it where to find the octicon method!

^ And run our test again.

---

[.background-color: #d73a49]
[.header: #ffffff]

# [fit] Expected element matching<br>".State.State--green", found 0

^ Interesting. It can't find the CSS we're looking for.

^ I wonder what our component is rendering.

---

```html
&lt;div class=&quot;State State--green&quot;...
```

^ It looks like our output is being escaped!

^ While it might be tempting to use html_safe here, that's probably not a good idea.

^ But what if we reused the existing Rails rendering pipeline?

---

[.code-highlight: 12-18]
[.code-highlight: 5-10]

```ruby
module Issues
  class Badge
    include OcticonsHelper

    def html
      eval(
        "output_buffer = ActionView::OutputBuffer.new;" +
        ActionView::Template::Handlers::ERB.erb_implementation.new(template, trim: true).src
      )
    end

    def template
      <<-erb
      <div class="State State--green">
        #{octicon('issue-opened')} Open
      </div>
      erb
    end
  end
end
```

^ First, let's move our template into a method called template.

^ S And in our html method, we'll run our template through ActionView's ERB template handler,

^ Effectively mirroring how regular Rails templates are compiled and then executed.

^ So let's run our tests again.

---

[.background-color: #28a745]
[.header: #ffffff]

^ There we go!

---

[.code-highlight: all]
[.code-highlight: 2]
[.code-highlight: 6]
[.code-highlight: 7]
[.code-highlight: 8]

```ruby
it "renders the closed issue badge" do
  create(:issue, :closed)

  get :index

  assert_select(".State.State--red")
  assert_select(".octicon-issue-closed")
  assert_includes(response.body, "Closed")
end
```

^ Let's keep moving along.

^ PAUSE

^ The next test is

^ S for a closed issue.

^ S Which should have a red background,

^ S closed icon,

^ S and "closed" label

^ Let's give it a run.

---

[.background-color: #d73a49]
[.header: #ffffff]

# [fit] Expected element matching<br>".State.State--red", found 0

^ It can't find the red CSS class, as we haven't handled this case yet.

^ Let's go back to our template that renders the component.

---

```erb
<%= render Issues::Badge, issue: issue, pull_request: issue.pull_request %>
```

^ We're already passing the issue into our component, but we aren't doing anything with it yet. Let's change that.

---

[.code-highlight: 3, 6]

```ruby
class ActionView::Base
  module RenderMonkeyPatch
    def render(component, *args)
      return super unless component == Issues::Badge

      component.new.html
    end
  end

  prepend RenderMonkeyPatch
end
```

^ First, we'll need to update our monkey patch

---

[.code-highlight: 3, 6]

```ruby
class ActionView::Base
  module RenderMonkeyPatch
    def render(component, *args)
      return super unless component == Issues::Badge

      component.new(*args).html
    end
  end

  prepend RenderMonkeyPatch
end
```

^ to pass the arguments through to our component's initializer.

---

[.code-highlight: 5-7]

```ruby
module Issues
  class Badge
    include OcticonsHelper

    def initialize(issue:, pull_request: nil)
      @issue = issue, @pull_request = pull_request
    end

    def html; end
    def template; end
  end
end
```

^ Next, we'll need to define an initialize method on our component.

^ We'll let pull_request be nil, as not all issues have pull requests.

---

[.code-highlight: all]
[.code-highlight: 10]

```ruby
module Issues
  class Badge
    include OcticonsHelper

    def initialize; end
    def html; end

    def template
      <<-erb
      <% if @issue.closed? %>
        <div class="State State--red">
          <%= octicon('issue-closed') %> Closed
        </div>
      <% else %>
        <div class="State State--green">
          <%= octicon('issue-opened') %> Open
        </div>
      <% end %>
      erb
    end
  end
end
```

^ Now that we have an issue,

^ S we can reference it in our template!

^ So let's run our test again...

---

[.background-color: #28a745]
[.header: #ffffff]

^ Phew. We're back to green.

^ But wait. Did you just see what we did there? We gave ourselves an interface!

---

# [fit] ~~Implicit<br>Arguments~~

^ Which means no more implicit arguments.

---

![fit](img/code-review-3.png)

^ And just like that, we're making progress on our code review!

---

```ruby
def template
  <<-erb
  <% if @pull_request && @pull_request.merged? %>
    <div class="State State--purple">
      <%= octicon('git-merge') %> Merged
    </div>
  <% elsif @pull_request && @pull_request.closed? %>
    <div class="State State--red">
      <%= octicon('git-pull-request') %> Closed
    </div>
  <% elsif @pull_request && @pull_request.draft? %>
    <div class="State">
    <%= octicon('git-pull-request') %> Draft
    </div>
  <% elsif @pull_request %>
    <div class="State State--green">
      <%= octicon('git-pull-request') %> Open
    </div>
  <% elsif @issue.closed? %>
    <div class="State State--red">
      <%= octicon('issue-closed') %> Closed
    </div>
  <% else %>
    <div class="State State--green">
      <%= octicon('issue-opened') %> Open
    </div>
  <% end %>
  erb
end
```

^ Next, we can drop in the rest of the original partial into our template method.

^ Now, let's see how the rest of our controller tests do.

---

[.background-color: #28a745]
[.header: #ffffff]

^ We're green!

---

[.code-highlight: all]
[.code-highlight: 1,5,9,13]
[.code-highlight: 17, 21]
[.code-highlight: all]

```erb
<% if @pull_request && @pull_request.merged? %>
  <div class="State State--purple">
    <%= octicon('git-merge') %> Merged
  </div>
<% elsif @pull_request && @pull_request.closed? %>
  <div class="State State--red">
    <%= octicon('git-pull-request') %> Closed
  </div>
<% elsif @pull_request && @pull_request.draft? %>
  <div class="State">
  <%= octicon('git-pull-request') %> Draft
  </div>
<% elsif @pull_request %>
  <div class="State State--green">
    <%= octicon('git-pull-request') %> Open
  </div>
<% elsif @issue.closed? %>
  <div class="State State--red">
    <%= octicon('issue-closed') %> Closed
  </div>
<% else %>
  <div class="State State--green">
    <%= octicon('issue-opened') %> Open
  </div>
<% end %>
```

^ But something doesn't seem right about our template.

^ S The first two thirds handle various pull request states

^ S While the last third handles issue state.

^ It seems as though we really have

^ S *two* components here, not one.

---

```erb
<%= render Issues::Badge, issue: issue, pull_request: issue.pull_request %>
```

^ Since the view that calls our component knows whether it is dealing with a pull request or an issue

^ How about we split this out into two components and let the view pick which one to use?

---

[.code-highlight: all]
[.code-highlight: 1]
[.code-highlight: 2]
[.code-highlight: 4]

```erb
<% if issue.pull_request %>
  <%= render PullRequests::Badge, pull_request: issue.pull_request %>
<% else %>
  <%= render Issues::Badge, issue: issue %>
<% end %>
```

^ That's not so bad!

^ S Based on whether the issue has a pull request, we can render either

^ S The pull request badge

^ S Or the issue badge

^ PAUSE

---

[.code-highlight: all]
[.code-highlight: 4]

```ruby
class ActionView::Base
  module RenderMonkeyPatch
    def render(component, *args)
      return super unless component == Issues::Badge

      component.new(*args).html
    end
  end

  prepend RenderMonkeyPatch
end
```

^ Back at our monkey patch

^ S We'll need to update our conditional

---

[.code-highlight: 4]

```ruby
class ActionView::Base
  module RenderMonkeyPatch
    def render(component, *args)
      return super unless [Issues::Badge, PullRequests::Badge].include?(component)

      component.new(*args).html
    end
  end

  prepend RenderMonkeyPatch
end
```

^ To look for both components.

^ Let's check on our tests

---

[.background-color: #28a745]
[.header: #ffffff]

^ Still green!

^ So let's go back to our code review.

---

![fit](img/code-review-2.png)

^ Remember that comment about magic strings?

---

[.code-highlight: 2, 6]

```erb
<% if @issue.closed? %>
  <div class="State State--red">
    <%= octicon('issue-closed') %> Closed
  </div>
<% else %>
  <div class="State State--green">
    <%= octicon('issue-opened') %> Open
  </div>
<% end %>
```

^ Both our issue badge

---

[.code-highlight: 2, 6, 10, 14]

```erb
<% if @pull_request && @pull_request.merged? %>
  <div class="State State--purple">
    <%= octicon('git-merge') %> Merged
  </div>
<% elsif @pull_request && @pull_request.closed? %>
  <div class="State State--red">
    <%= octicon('git-pull-request') %> Closed
  </div>
<% elsif @pull_request && @pull_request.draft? %>
  <div class="State">
    <%= octicon('git-pull-request') %> Draft
  </div>
<% else %>
  <div class="State State--green">
    <%= octicon('git-pull-request') %> Open
  </div>
<% end %>
```

^ And our pull request badge are rendering the same State UI element from our design system.

^ So why not make that a component?

---

[.code-highlight: all]
[.code-highlight: 1]

```erb
<div class="State State--green">
  <%= octicon('git-pull-request') %> Open
</div>
```

^ Our State UI element really just has one option:

^ S color.

^ So if it was a component,

---

[.code-highlight: 1]
```erb
<%= render Primer::State, color: :green do %>
  <%= octicon('git-pull-request') %> Open
<% end %>
```

^ That would be our single argument

^ So let's build it!

---

```ruby
module Primer
  class State
  end
end
```

^ We'll call it State, inside the Primer module.

---

[.code-highlight: 4]

```ruby
class ActionView::Base
  module RenderMonkeyPatch
    def render(component, *args)
      return super unless [Issues::Badge, PullRequests::Badge].include?(component)

      component.new(*args).html
    end
  end

  prepend RenderMonkeyPatch
end
```

^ We'll also need to update our monkey patch

---

[.code-highlight: 4]

```ruby
class ActionView::Base
  module RenderMonkeyPatch
    def render(component, *args)
      return super unless [Issues::Badge, PullRequests::Badge, Primer::State].include?(component)

      component.new(*args).html
    end
  end

  prepend RenderMonkeyPatch
end
```

^ to handle yet another component.

^ But wait, that doesn't feel right.

^ Perhaps we're missing an abstraction here.

^ What we're really trying to say is: "Am I dealing with one of these newfangled components?"

^ Perhaps it's time for a parent class!

---

```ruby
module ActionView
  class Component < ActionView::Base
  end
end
```

^ Enter ActionView::Component.

^ PAUSE

^ So let's take our new parent class...

---

[.code-highlight: 2, 7, 12]

```ruby
module Issues
  class Badge < ActionView::Component
  end
end

module PullRequests
  class Badge < ActionView::Component
  end
end

module Primer
  class State < ActionView::Component
  end
end
```

^ And update our existing components to inherit from it.

---

[.code-highlight: 4]

```ruby
class ActionView::Base
  module RenderMonkeyPatch
    def render(component, *args)
      return super unless [Issues::Badge, PullRequests::Badge, Primer::State].include?(component)

      component.new(*args).html
    end
  end

  prepend RenderMonkeyPatch
end
```

^ Then, we can simplify the conditional in our monkey patch

---

[.code-highlight: 4]

```ruby
class ActionView::Base
  module RenderMonkeyPatch
    def render(component, *args)
      return super unless component < ActionView::Component

      component.new(*args).html
    end
  end

  prepend RenderMonkeyPatch
end
```

^ To just check if the argument is a subclass of ActionView::Component.

^ So now that we have a parent class for our components, let's try to reduce some duplication.

---

[.code-highlight: 3-8]

```ruby
module Issues
  class Badge
    def html
      eval(
        "output_buffer = ActionView::OutputBuffer.new; " +
        ActionView::Template::Handlers::ERB.erb_implementation.new(template, trim: true).src
      )
    end
  end
end
```

^ An easy candidate is our html method, which does not have any component specific logic.

---

```ruby
module ActionView
  class Component < ActionView::Base
    def html
      eval(
        "output_buffer = ActionView::OutputBuffer.new; " +
        ActionView::Template::Handlers::ERB.erb_implementation.new(template, trim: true).src
      )
    end
  end
end
```

^ So let's move that to ActionView::Component.

^ And let's run our tests again:

---

[.background-color: #28a745]
[.header: #ffffff]

^ Still green.

---

[.code-highlight: all]
[.code-highlight: 2]

```erb
<%= render Primer::State, color: :green do %>
  <%= octicon('git-pull-request') %> Open
<% end %>
```

^ Back to building our new component.

^ PAUSE

^ This one's a little different:

^ S We're passing it content as a block.

^ PAUSE

^ So let's start by writing a test.

---

^ Now while we could probably just rely on the existing controller tests for this

^ Wouldn't it be nice if we could test this new, nested component by itself?

---

[.code-highlight: all]
[.code-highlight: 2]
[.code-highlight: 3]

```jsx
it('should render the closed issue badge', function() {
  expect(shallow(<IssueBadge props={{ issue: { isClosed: true }}} />).
  contains(<div className="State State--red">Closed</div>)).toBe(true);
});
```

^ In React, our tests

^ S were able to render our component directly,

^ S then assert against the resulting HTML.

^ Ideally, we'd be able to do...

---

[.code-highlight: all]
[.code-highlight: 2]
[.code-highlight: 4]
[.code-highlight: 2]

```ruby
it "renders content passed to it as a block" do
  result = render_string("<%= render Primer::State do %>content<% end %>")

  assert_includes result.css(".State.State--green").text, "content"
end
```

^ the same in Rails:

^ S Render the component directly,

^ S and then assert against the resulting HTML.

^ S All we need is a way to render a template inline.

---

[.code-highlight: all]
[.code-highlight: 2]
[.code-highlight: 4]

```ruby
def render_string(string)
  html = ApplicationController.new.view_context.render(inline: string)

  Nokogiri::HTML(html)
end
```

^ Which we can do via ApplicationController,

^ S Rendering our template in the same code path as a normal view, and then

^ S Parsing the result in Nokogiri for easier assertions.

^ PAUSE

^ So let's run our test now.

---

[.background-color: #d73a49]
[.header: #ffffff]

# [fit] no implicit conversion<br>of Class into Hash

^ Sounds like something that expects a Class is recieving a Hash!

---

[.code-highlight: all]
[.code-highlight: 2]

```ruby
def render_string(string)
  html = ApplicationController.new.view_context.render(inline: string)

  Nokogiri::HTML(html)
end
```

^ And it looks like our test helper is to blame,

^ S passing a hash to #render.

^ It turns out that ActionView's #render method accepts a couple different types of arguments

---

[.code-highlight: 3, 4]

```ruby
class ActionView::Base
  module RenderMonkeyPatch
    def render(component, *args)
      return super unless component < ActionView::Component

      component.new(*args).html
    end
  end

  prepend RenderMonkeyPatch
end
```

^ So let's go back to our monkey patch,

---

[.code-highlight: 3, 4]

```ruby
class ActionView::Base
  module RenderMonkeyPatch
    def render(component, *args)
      return super unless component.is_a?(Class) && component < ActionView::Component

      component.new(*args).html
    end
  end

  prepend RenderMonkeyPatch
end
```

^ and update our conditional to make sure we're dealing with a Class, then re-run our tests.

---

[.background-color: #d73a49]
[.header: #ffffff]

# [fit] Expected " " to include "content".

^ There we go!

^ Where we were expecting our content to be rendered, we just got an empty string.

^ So let's think about how we might make this work.

---

[.code-highlight: all]
[.code-highlight: 2]
[.code-highlight: 1,3]

```erb
<%= render Issues::Badge, color: :green do %>
  <%= octicon('issue-opened') %> Open
<% end %>
```

^ When we're passing content into our component, what we're effectively saying is:

^ S "render this block in the context of the current view", then

^ S "Wrap the result in the component"

^ So how might that look?

---

[.code-highlight: 3]

```ruby
class ActionView::Base
  module RenderMonkeyPatch
    def render(component, *args)
      return super unless component.is_a?(Class) && component < ActionView::Component

      component.new(*args).html
    end
  end

  prepend RenderMonkeyPatch
end
```

^ First, we'll need to update our monkey patch

---

[.code-highlight: 3]

```ruby
class ActionView::Base
  module RenderMonkeyPatch
    def render(component, *args, &block)
      return super unless component.is_a?(Class) && component < ActionView::Component

      component.new(*args).html
    end
  end

  prepend RenderMonkeyPatch
end
```

^ To accept a block argument.

---

[.code-highlight: 6]

```ruby
class ActionView::Base
  module RenderMonkeyPatch
    def render(component, *args, &block)
      return super unless component.is_a?(Class) && component < ActionView::Component

      component.new(*args).html
    end
  end

  prepend RenderMonkeyPatch
end
```

^ Then we'll need to update our render step

---

[.code-highlight: 6]
[.code-highlight: 7]
[.code-highlight: 8]

```ruby
class ActionView::Base
  module RenderMonkeyPatch
    def render(component, *args, &block)
      return super unless component.is_a?(Class) && component < ActionView::Component

      instance = component.new(*args)
      instance.content = self.capture(&block) if block_given?
      instance.html
    end
  end

  prepend RenderMonkeyPatch
end
```

^ To first instantiate the component

^ S Then, if a block has been passed, render it in the context of the current view, using ActionView's capture helper, and assign the result to an accessor on the component.

^ At that point, our component will know about the content

^ S so we can render it.

^ So since we're expecting all components to have a content accessor,

---

```ruby
module ActionView
  class Component < ActionView::Base
    def html
      eval(
        "output_buffer = ActionView::OutputBuffer.new; " +
        ActionView::Template::Handlers::ERB.erb_implementation.new(template, trim: true).src
      )
    end
  end
end
```

^ Let's go back to ActionView::Component

---

[.code-highlight: 3]

```ruby
module ActionView
  class Component < ActionView::Base
    attr_accessor :content

    def html
      eval(
        "output_buffer = ActionView::OutputBuffer.new; " +
        ActionView::Template::Handlers::ERB.erb_implementation.new(template, trim: true).src
      )
    end
  end
end
```

^ And declare it there.

---

```ruby
module Primer
  class State < ActionView::Component
    def template
      <<-erb
      <div class="State State--green">
      </div>
      erb
    end
  end
end
```

^ Then, it's just a matter of taking our component

---

[.code-highlight: 6]

```ruby
module Primer
  class State < ActionView::Component
    def template
      <<-erb
      <div class="State State--green">
        <%= content %>
      </div>
      erb
    end
  end
end
```

^ And updating the template to render the value of the content accessor.

^ But let's see about our test.

---

[.background-color: #28a745]
[.header: #ffffff]

^ We're back to green!

---

[.code-highlight: all]
[.code-highlight: 5]

```ruby
module Primer
  class State < ActionView::Component
    def template
      <<-erb
      <div class="State State--green">
        <%= content %>
      </div>
      erb
    end
  end
end
```

^ Now that we have content,

^ S what about setting the color?

---

[.code-highlight: 3-5]

```ruby
module Primer
  class State < ActionView::Component
    def initialize(color:)
      @color = color
    end

    def template
      <<-erb
      <div class="State State--green">
        <%= content %>
      </div>
      erb
    end
  end
end
```

^ Let's start by adding a color argument to the initializer.

^ But what values do we need to handle?

---

![fit](img/primer-state-docs-colors.png)

^ Let's look at the docs!

---

![fit](img/primer-state-docs-colors-highlighted.png)

^ It looks like we can specify three: green, red, and purple. Otherwise, the component defaults to grey.

---

[.code-highlight: all]

```ruby
module Primer
  class State < ActionView::Component
    def initialize(color:)
      @color = color
    end

    def template
      <<-erb
      <div class="State State--green">
        <%= content %>
      </div>
      erb
    end
  end
end
```

^ So let's go back to our component

---

[.code-highlight: 3-8]
[.code-highlight: 4]
[.code-highlight: 5-7]
[.code-highlight: 4-7]

```ruby
module Primer
  class State < ActionView::Component
    COLOR_CLASS_MAPPINGS = {
      default: "",
      green: "State--green",
      red: "State--red",
      purple: "State--purple",
    }.freeze

    def initialize; end
    def template; end
  end
end
```

^ And capture those relationships in a constant.

^ This gives a clear mapping between the:

^ S default value and not applying a CSS class, and between

^ S the color values and their respective CSS classes.

^ S The keys of our hash also represent the entirety of the values we should allow for the color argument

^ So how can we enforce this in our component?

---

[.code-highlight: all]
[.code-highlight: 3]
[.code-highlight: 2-4]
[.code-highlight: 6]

```ruby
it "raises an error when color is not one of valid values" do
  exception = assert_raises ActionView::Template::Error do
    render_string("<%= render Primer::State, color: :chartreuse do %>foo<% end %>")
  end

  assert_includes exception.message, "Color is not included in the list"
end
```

^ Let's start with a test.

^ S We'll assert that when passing in a color we're not expecting

^ S an error will be raised

^ S with a message in a format that is suspiciously familiar

^ So let's run it...

---

[.background-color: #d73a49]
[.header: #ffffff]

# [fit] ActionView::Template::Error<br>expected but nothing was raised.

^ And make sure it fails.

---

^ So how might we ensure color is one of our expected values?

^ We're in Rails, so that's a solved problem:

---

# [fit] ActiveModel::Validation

^ ActiveModel validations!

---

[.code-highlight: all]

```ruby
module Primer
  class State < ActionView::Component
    COLOR_CLASS_MAPPINGS = {
      default: "",
      green: "State--green",
      red: "State--red",
      purple: "State--purple",
    }.freeze

    def initialize; end
    def template; end
  end
end
```

^ Back in our component,

---

[.code-highlight: 10]

```ruby
module Primer
  class State < ActionView::Component
    COLOR_CLASS_MAPPINGS = {
      default: "",
      green: "State--green",
      red: "State--red",
      purple: "State--purple",
    }.freeze

    validates :color, inclusion: { in: COLOR_CLASS_MAPPINGS.keys }

    def initialize; end
    def template; end
  end
end
```

^ We can use an inclusion validation to check that color is one of the keys in our constant.

^ PAUSE

---

[.code-highlight: 10, 11]

```ruby
module Primer
  class State < ActionView::Component
    COLOR_CLASS_MAPPINGS = {
      default: "",
      green: "State--green",
      red: "State--red",
      purple: "State--purple",
    }.freeze

    attr_reader :color
    validates :color, inclusion: { in: COLOR_CLASS_MAPPINGS.keys }

    def initialize; end
    def template; end
  end
end
```

^ To make this work, we'll need to define an attribute reader.

---

```ruby
module ActionView
  class Component < ActionView::Base
    attr_accessor :content

    def html
      eval(
        "output_buffer = ActionView::OutputBuffer.new; " +
        ActionView::Template::Handlers::ERB.erb_implementation.new(template, trim: true).src
      )
    end
  end
end
```

^ And in ActionView::Component,

---

[.code-highlight: 3]

```ruby
module ActionView
  class Component < ActionView::Base
    include ActiveModel::Validations
    attr_accessor :content

    def html
      eval(
        "output_buffer = ActionView::OutputBuffer.new; " +
        ActionView::Template::Handlers::ERB.erb_implementation.new(template, trim: true).src
      )
    end
  end
end
```

^ We'll include ActiveModel Validations.

---

```ruby
class ActionView::Base
  module RenderMonkeyPatch
    def render(component, *args, &block)
      return super unless component.is_a?(Class) && component < ActionView::Component

      instance = component.new(*args)
      instance.content = self.capture(&block) if block_given?
      instance.render
    end
  end

  prepend RenderMonkeyPatch
end
```

^ All that's left is to go back to our monkey patch

---

[.code-highlight: 8]
[.code-highlight: 8, 9]

```ruby
class ActionView::Base
  module RenderMonkeyPatch
    def render(component, *args, &block)
      return super unless component.is_a?(Class) && component < ActionView::Component

      instance = component.new(*args)
      instance.content = self.capture(&block) if block_given?
      instance.validate!
      instance.html
    end
  end

  prepend RenderMonkeyPatch
end
```

^ And add a step to validate our component

^ S before we render it.

^ PAUSE

^ So let's run our test again.

---

[.background-color: #28a745]
[.header: #ffffff]

^ Back to green.

---

[.code-highlight: all]
[.code-highlight: 4]
[.code-highlight: 2]

```ruby
it "assigns the correct CSS class for color" do
  result = render_string("<%= render Primer::State, color: :purple do %>content<% end %>")

  assert result.css(".State.State--purple").any?
end
```

^ So now let's add a test to make sure we're

^ S setting the right CSS class

^ S based on the color

---

[.background-color: #d73a49]
[.header: #ffffff]

# [fit] Expected false to be truthy.

^ And that our test fails.

---

[.code-highlight: all]
[.code-highlight: 15]
[.code-highlight: 11]

```ruby
module Primer
  class State < ActionView::Component
    COLOR_CLASS_MAPPINGS = {
      default: "",
      green: "State--green",
      red: "State--red",
      purple: "State--purple",
    }.freeze

    attr_reader :color
    validates :color, inclusion: { in: COLOR_CLASS_MAPPINGS.keys }

    def template
      <<-erb
      <div class="State State--green">
        <%= content %>
      </div>
      erb
    end
  end
end
```

^ Previously,

^ S we just had the CSS class hardcoded.

^ S But now that we can be sure that color is one of the keys in our hash,

---

[.code-highlight: 21-23]

```ruby
module Primer
  class State < ActionView::Component
    COLOR_CLASS_MAPPINGS = {
      default: "",
      green: "State--green",
      red: "State--red",
      purple: "State--purple",
    }.freeze

    attr_reader :color
    validates :color, inclusion: { in: COLOR_CLASS_MAPPINGS.keys }

    def template
      <<-erb
      <div class="State State--green">
        <%= content %>
      </div>
      erb
    end

    def class_name
      COLOR_CLASS_MAPPINGS[color]
    end
  end
end
```

^ We can safely use the hash to look up the correct CSS class.

---

[.code-highlight: 15]

```ruby
module Primer
  class State < ActionView::Component
    COLOR_CLASS_MAPPINGS = {
      default: "",
      green: "State--green",
      red: "State--red",
      purple: "State--purple",
    }.freeze

    attr_reader :color
    validates :color, inclusion: { in: COLOR_CLASS_MAPPINGS.keys }

    def template
      <<-erb
      <div class="State <%= class_name %>">
        <%= content %>
      </div>
      erb
    end

    def class_name
      COLOR_CLASS_MAPPINGS[color]
    end
  end
end
```

^ And use it in our template.

---

[.background-color: #28a745]
[.header: #ffffff]

^ And we're back to green.

^ So let's take another look at our design system docs:

---

![fit](img/primer-state-docs-title.png)

^ PAUSE

^ I think we might have missed something.

---

![fit](img/primer-state-docs-title-highlighted.png)

^ We're supposed to have a title attribute!

^ For most of our Primer components, CSS classes are not the entire interface.

^ But this is something our original partial never accounted for.

^ So let's make sure that doesn't happen again.

---

[.code-highlight: all]
[.code-highlight: 3]
[.code-highlight: 6]

```ruby
it "raises an error when title is not present" do
  exception = assert_raises ActionView::Template::Error do
    render_string("<%= render Primer::State, title: '' do %>foo<% end %>")
  end

  assert_includes exception.message, "Title can't be blank"
end
```

^ We'll do that with a test

^ S that passes in an empty title

^ S and then expects a validation error.

---

[.background-color: #d73a49]
[.header: #ffffff]

# [fit] Expected false to be truthy.

^ And make sure it fails.

---

[.code-highlight: 3-4]

```ruby
module Primer
  class State < ActionView::Component
    attr_reader :title
    validates :title, presence: true
  end
end
```

^ Then it's just a matter of adding a presence validation for the title attribute.

---

[.background-color: #28a745]
[.header: #ffffff]

^ And we're back to green.

^ But let's see how our controller tests fare:

---

[.background-color: #d73a49]
[.header: #ffffff]

# [fit] missing keyword: title

^ Missing keyword: title?

^ I think we just caught a regression!

---

[.code-highlight: 6, 10]

```erb
module Issues
  class Badge < ActionView::Component
    def template
      <<-erb
      <% if @issue.closed? %>
        <%= render Primer::State, color: :red do %>
          <%= octicon('issue-closed') %> Closed
        <% end %>
      <% else %>
        <%= render Primer::State, color: :green do %>
          <%= octicon('issue-opened') %> Open
        <% end %>
      <% end %>
      erb
    end
  end
end
```

^ We never updated our consumers of Primer::State to pass in the required title argument!

---

[.code-highlight: 6, 10]

```erb
module Issues
  class Badge < ActionView::Component
    def template
      <<-erb
      <% if @issue.closed? %>
        <%= render Primer::State, color: :red, title: "Status: Closed" do %>
          <%= octicon('issue-closed') %> Closed
        <% end %>
      <% else %>
        <%= render Primer::State, color: :green, title: "Status: Open" do %>
          <%= octicon('issue-opened') %> Open
        <% end %>
      <% end %>
      erb
    end
  end
end
```

^ So let's add the title attribute.

---

[.background-color: #28a745]
[.header: #ffffff]

^ And we're back to green.

---

# [fit] Data Flow

^ So when it comes to data flow, we were mainly concerned with

---

# [fit] N + 1

^ our views unintentionally querying the database.

^ But what if we could avoid passing in ActiveRecord objects at all? That would eliminate the risk.

---

[.code-highlight: all]
[.code-highlight: 5-7]
[.code-highlight: 11]

```ruby
module Issues
  class Badge < ActionView::Component
    include OcticonsHelper

    def initialize(issue:)
      @issue = issue
    end

    def template
      <<-erb
      <% if @issue.closed? %>
        <%= render Primer::State, color: :red, title: "Status: Closed" do %>
          <%= octicon('issue-closed') %> Closed
        <% end %>
      <% else %>
        <%= render Primer::State, color: :green, title: "Status: Open" do %>
          <%= octicon('issue-opened') %> Open
        <% end %>
      <% end %>
      erb
    end
  end
end
```

^ Let's start with Issue::Badge.

^ S Right now, we're passing in an issue, which is an ActiveRecord object.

^ S But the only thing we're doing with it is calling the #closed predicate method

^ As you can probably imagine, Issue's interface is much more than just this one method

^ but yet we're passing the entire object in just to get one value!

---

[.code-highlight: all]
[.code-highlight: 3]

```ruby
class Issue < ApplicationRecord
  def closed?
    state == "closed"
  end
end
```

^ Looking at the implementation of the closed predicate method,

^ S it's just checking whether the value is "closed".

^ What might our component look like if we passed in the state value instead of the whole issue object?

---

[.code-highlight: 5-7]

```ruby
module Issues
  class Badge < ActionView::Component
    include OcticonsHelper

    def initialize(issue:)
      @issue = issue
    end

    def template
      <<-erb
      <% if @issue.closed? %>
        <%= render Primer::State, color: :red, title: "Status: Closed" do %>
          <%= octicon('issue-closed') %> Closed
        <% end %>
      <% else %>
        <%= render Primer::State, color: :green, title: "Status: Open" do %>
          <%= octicon('issue-opened') %> Open
        <% end %>
      <% end %>
      erb
    end
  end
end
```

^ First, we'd have to update the initialize method to

---

[.code-highlight: 5-7]

```ruby
module Issues
  class Badge < ActionView::Component
    include OcticonsHelper

    def initialize(state:)
      @state = state
    end

    def template
      <<-erb
      <% if @issue.closed? %>
        <%= render Primer::State, color: :red, title: "Status: Closed" do %>
          <%= octicon('issue-closed') %> Closed
        <% end %>
      <% else %>
        <%= render Primer::State, color: :green, title: "Status: Open" do %>
          <%= octicon('issue-opened') %> Open
        <% end %>
      <% end %>
      erb
    end
  end
end
```

^ Accept the state *value* instead of the issue *object*,...

---

[.code-highlight: 5-6]

```ruby
module Issues
  class Badge < ActionView::Component
    include OcticonsHelper

    attr_reader :state
    validates :state, inclusion: { in: [:open, :closed] }

    def initialize(state:)
      @state = state
    end

    def template
      <<-erb
      <% if @issue.closed? %>
        <%= render Primer::State, color: :red, title: "Status: Closed" do %>
          <%= octicon('issue-closed') %> Closed
        <% end %>
      <% else %>
        <%= render Primer::State, color: :green, title: "Status: Open" do %>
          <%= octicon('issue-opened') %> Open
        <% end %>
      <% end %>
      erb
    end
  end
end
```

^ And add a validation.

^ PAUSE

---

[.code-highlight: 3-16]

```ruby
module Issues
  class Badge < ActionView::Component
    def template
      <<-erb
      <% if @issue.closed? %>
        <%= render Primer::State, color: :red, title: "Status: Closed" do %>
          <%= octicon('issue-closed') %> Closed
        <% end %>
      <% else %>
        <%= render Primer::State, color: :green, title: "Status: Open" do %>
          <%= octicon('issue-opened') %> Open
        <% end %>
      <% end %>
      erb
    end
  end
end
```

^ Looking at our template, what if we extracted each branch to be derived from the value of state?

---

[.code-highlight: 5-16]
[.code-highlight: 6, 11]
[.code-highlight: 7-9, 12-14]


```ruby
module Issues
  class Badge < ActionView::Component
    include OcticonsHelper

    STATES = {
      open: {
        color: :green,
        octicon_name: "issue-opened",
        label: "Open"
      },
      closed: {
        color: :red,
        octicon_name: "issue-closed",
        label: "Closed"
      }
    }.freeze

    attr_reader :state
    validates :state, inclusion: { in: STATES.keys }

    def initialize; end
    def template; end
  end
end
```

^ We could clearly express the relationship between

^ S the state

^ S and the combination of color, icon name, and label.

---

[.code-highlight: 3-15]

```ruby
module Issues
  class Badge < ActionView::Component
    def template
      <<-erb
      <% if @issue.closed? %>
        <%= render Primer::State, color: :red, title: "Status: Closed" do %>
          <%= octicon('issue-closed') %> Closed
        <% end %>
      <% else %>
        <%= render Primer::State, color: :green, title: "Status: Open" do %>
          <%= octicon('issue-opened') %> Open
        <% end %>
      <% end %>
      erb
    end
  end
end
```

^ Then, we can take our template,

---

[.code-highlight: 3-21]

```ruby
module Issues
  class Badge < ActionView::Component
    def template
      <<-erb
      <%= render Primer::State, color: color, title: "Status: #{label}" do %>
        <%= octicon(octicon_name) %> <%= label %>
      <% end %>
      erb
    end

    def color
      STATES[state][:color]
    end

    def octicon_name
      STATES[state][:octicon_name]
    end

    def label
      STATES[state][:label]
    end
  end
end
```

^ And extract the values from the constant, instead of having nearly duplicate branches in our template.

^ So let's run our tests...

---

[.background-color: #28a745]
[.header: #ffffff]

^ And we're still green.

---

^ But what about our pull request component?

^ How might we decouple it from ActiveRecord?

---

[.code-highlight: 5-7]

```ruby
module PullRequests
  class Badge < ActionView::Component
    def template
      <<-erb
      <% if pull_request.merged? %>
      <% elsif pull_request.closed? %>
      <% elsif pull_request.draft? %>
      <% else %>
      <% end %>
      erb
    end
  end
end
```

^ Looking at the template, we're relying on three predicate methods: merged, closed and draft.

^ So can we pass in a state value like we did for the issue component?

---

[.code-highlight: all]
[.code-highlight: 2-6]
[.code-highlight: 8-9]
[.code-highlight: 2-9]

```ruby
class PullRequest < ApplicationRecord
  def state
    return :open     if open?
    return :merged   if merged?
    return :closed   if closed?
  end

  # autogenerated
  def draft?; end
end
```

^ Looking at the pull request model, things aren't as simple as they were for the issue model

^ S While we do have a state value,

^ S Whether the pull request is a draft or not is independent of the state value. (In fact, it's just a boolean in the schema)

^ S Which means we'll need both of these values to render the pull request component.

^ So let's start with some tests:

---

[.code-highlight: all]
[.code-highlight: 2]
[.code-highlight: 4]
[.code-highlight: 5]
[.code-highlight: 6]

```ruby
it "renders the draft state" do
  result = render_string("<%= render PullRequests::Badge, state: :open, is_draft: true %>")

  assert_includes result.text, "Draft"
  assert result.css("[title='Status: Draft']").any?
  assert result.css(".octicon-git-pull-request").any?
end

it "renders the closed draft state"
it "renders the merged state"
it "renders the closed state"
it "renders the open state"
```

^ In this first one,

^ S we'll assert that when we pass in state and is_draft values,

^ S We render the correct label

^ S title attribute

^ S and icon

^ Let's run them!

---

[.background-color: #d73a49]
[.header: #ffffff]

# [fit] missing keyword: pull_request

^ It looks like our component is still expecting the old argument.

^ Let's go update it!

---

[.code-highlight: 3]

```ruby
module PullRequests
  class Badge < ActionView::Component
    def initialize(pull_request:)
      @pull_request = pull_request
    end
  end
end
```

^ First, we'll need to update the initializer

---

[.code-highlight: 3]

```ruby
module PullRequests
  class Badge < ActionView::Component
    def initialize(state:, is_draft:)
      @state, @is_draft = state, is_draft
    end
  end
end
```

^ To accept the state and is_draft *values*, instead of the pull request *object*.

---

[.code-highlight: 5-21]

```ruby
module PullRequests
  class Badge < ActionView::Component
    def template
      <<-erb
      <% if pull_request.merged? %>
        <%= render Primer::State, color: :purple, title: "Status: Merged" do %>
          <%= octicon('git-merge') %> Merged
        <% end %>
      <% elsif pull_request.closed? %>
        <%= render Primer::State, color: :red, title: "Status: Closed" do %>
          <%= octicon('git-pull-request') %> Closed
        <% end %>
      <% elsif pull_request.draft? %>
        <%= render Primer::State, color: :default, title: "Status: Draft" do %>
          <%= octicon('git-pull-request') %> Draft
        <% end %>
      <% else %>
        <%= render Primer::State, color: :green, title: "Status: Open" do %>
          <%= octicon('git-pull-request') %> Open
        <% end %>
      <% end %>
      erb
    end
  end
end
```

^ So now let's take our template

---

```ruby
module PullRequests
  class Badge < ActionView::Component
    def template
      <<-erb
      <%= render Primer::State, title: title, color: color do %>
        <%= octicon(octicon_name) %> <%= label %>
      <% end %>
      erb
    end

    def title; end
    def color; end
    def octicon_name; end
    def label; end
  end
end
```

^ And extract the title, color, octicon name, and label into methods.

^ PAUSE

^ What's interesting here, is that...

---

```jsx
class IssueBadge extends React.Component {
  render() {
    return (
      <div className={ "State " + this._stateClass() }>
        <i className={this._icon()} /> {this._label()}
      </div>
    )
  }

  _icon() { ... }
  _stateClass() { ... }
  _label() { ... }
}
```

^ looking back at our original React mockup, it's almost uncanny how similar the two are!

---

^ So let's see how our tests fare:

---

[.background-color: #28a745]
[.header: #ffffff]

^ Back to green!

---

# [fit] Data Flow

^ So remember how React encouraged simple data flow, minimizing side-affects?

---

# [fit] Values > Objects

^ By passing *values* into our components instead of *objects*, we're seeing similar benefits.

---

# [fit] Code<br>Coverage

^ And remember how we were unable to get coverage reports for our views?

---

![fit](img/coverage-score.png)

^ Our app now has a perfect score in SimpleCov.

---

![fit](img/pull-request-component-coverage.png)

^ Digging into the report, we now have proof that all of the branching logic in our pull request component is being exercised.

---

^ PAUSE

---

# [fit] Performance

^ So what about performance?

---

# [fit] Benchmark

^ What might a useful benchmark be?

---

# [fit] Nested Partials

^ Let's compare our implementation to rendering nested partials.

---

[.code-highlight: all]
[.code-highlight: 2]
[.code-highlight: 1,3]

```erb
<div class="Box p-2">
  <%= yield %>
</div>
```

^ So given a partial

^ S that wraps the content passed to it

^ S in a box element from our design system

---

[.code-highlight: all]
[.code-highlight: 6-8]

```ruby
class Box < ActionView::Component
  validates :content, presence: true

  def self.template
    <<-erb
    <div class="Box p-2">
      <%= content %>
    </div>
    erb
  end
end
```

^ And a component

^ S that does the same...

---

[.code-highlight: all]
[.code-highlight: 1]
[.code-highlight: 2-14]
[.code-highlight: 15-27]
[.code-highlight: 28]

```erb
<% Benchmark.ips do |x| %>
  <% x.report("component") do %>
    <%= render Box do %>
      <%= render Box do %>
        <%= render Box do %>
          <%= render Box do %>
            <%= render Box do %>
              <%= render Box do %>
                <%= render Box do %>
                  <%= render Box do %>
                    <%= render Box.do %>
                      <%= render Box do %>
    ...
  <% end %>
  <% x.report("partial") do %>
    <%= render "box" do %>
      <%= render "box" do %>
        <%= render "box" do %>
          <%= render "box" do %>
            <%= render "box" do %>
              <%= render "box" do %>
                <%= render "box" do %>
                  <%= render "box" do %>
                    <%= render "box" do %>
                      <%= render "box" do %>
    ...
  <% end %>
  <%= x.compare! %>
<% end %>
```

^ We can construct a stress test!

^ S Using Evan Phoenix's benchmark IPS gem

^ S We'll render ten nested box components

^ S and ten nested box partials

^ S and compare the result...

---

```
Comparison:
           component:     6531.5 i/s
             partial:     1289.4 i/s - 5.07x  slower
```

^ As it turns out, rendering components is five times faster than rendering partials!

---

# [fit] Testing

^ What about test performance?

---

# [fit] 6s

^ In our test suite, controller tests take about six seconds for loading a page and asserting against the content.

^ What about our new unit tests?

---

# [fit] 25ms

^ They clocked in at around 25 milliseconds, running in the same suite.

---

# [fit] 240x

^ That’s two-hundred and fourty times faster.

---

# [fit] Production?

^ So what are we waiting for, let's ship it!

^ As it turns out, we already have!

---

# [fit] :ship: Mid-March

^ The components we've written today have been running in production since March.

---

![fit](img/component-usage-cropped.png)

^ We're also rendering Repository Topics and Language Badges with ActionView::Component.

^ PAUSE

---

# [fit] Lessons

^ So what have we learned since then?

---

# [fit] API

^ So we've simplified the API a bit.

---

[.code-highlight: all]
[.code-highlight: 3]
[.code-highlight: 6]

```ruby
class ActionView::Base
  module RenderMonkeyPatch
    def render(component, *args, &block)
      return super unless component.is_a?(Class) && component < ActionView::Component

      instance = component.new(*args)
      instance.content = self.capture(&block) if block_given?
      instance.validate!
      instance.html
    end
  end

  prepend RenderMonkeyPatch
end
```

^ Looking back at our monkey patch

^ S We were taking the arguments

^ $ And then almost immediately instantiating the component with them.

^ This indirection began to stick out as confusing and unnecessary...

^ So we removed it!

---

[.code-highlight: 1]

```erb
<%= render Issues::Badge, color: :green do %>
  <%= octicon('issue-opened') %> Open
<% end %>
```

^ So instead of passing the component arguments

^ after the component name

---

[.code-highlight: 1]

```erb
<%= render Issues::Badge.new(color: :green) do %>
  <%= octicon('issue-opened') %> Open
<% end %>
```

^ We instead instantiate the component with the arguments

^ before passing it to render.

---

# [fit] Templates

^ We also ran into an issue with templates:

^ Support for syntax highlighting HEREDOCs is not universal

---

![fit](img/bad-heredoc-highlighting.png)

^ We don't even do it properly!

---

`pull_requests/badge.rb`

```ruby
module PullRequests
  class Badge < ActionView::Component
    def template
      <<-erb
      <% if pull_request.merged? %>
        <%= render Primer::State, color: :purple, title: "Status: Merged" do %>
          <%= octicon('git-merge') %> Merged
        <% end %>
      <% elsif pull_request.closed? %>
        <%= render Primer::State, color: :red, title: "Status: Closed" do %>
          <%= octicon('git-pull-request') %> Closed
        <% end %>
      <% elsif pull_request.draft? %>
        <%= render Primer::State, color: :default, title: "Status: Draft" do %>
          <%= octicon('git-pull-request') %> Draft
        <% end %>
      <% else %>
        <%= render Primer::State, color: :green, title: "Status: Open" do %>
          <%= octicon('git-pull-request') %> Open
        <% end %>
      <% end %>
      erb
    end
  end
end
```

^ We also found that having a template inline in a component got awkward when the template was more than a dozen lines or so.

^ So with those problems in mind,

^ We added the ability to take that inline template

---

`pull_requests/badge.html.erb`

```erb
<% if pull_request.merged? %>
  <%= render Primer::State, color: :purple, title: "Status: Merged" do %>
    <%= octicon('git-merge') %> Merged
  <% end %>
<% elsif pull_request.closed? %>
  <%= render Primer::State, color: :red, title: "Status: Closed" do %>
    <%= octicon('git-pull-request') %> Closed
  <% end %>
<% elsif pull_request.draft? %>
  <%= render Primer::State, color: :default, title: "Status: Draft" do %>
    <%= octicon('git-pull-request') %> Draft
  <% end %>
<% else %>
  <%= render Primer::State, color: :green, title: "Status: Open" do %>
    <%= octicon('git-pull-request') %> Open
  <% end %>
<% end %>
```

^ And define it in a sidecar file instead

^ PAUSE

---

# [fit] Convention

^ But perhaps the most exciting thing we've learned is about convention

---

^ So you know how a lot of Rails apps end up with a couple unconventional folders in the app directory?

^ There often ends up being one that is view-related. It's a place to put logic that doesn't seem to make sense in models, controllers, or views.

^ Usually it's something like

---

# [fit] Presenters

^ Presenters

---

# [fit] Decorators

^ Decorators

---

# [fit] View Models

^ Or view models

^ Ours happens to be view models.

---

# [fit] ~700

^ We have around 700 of them!

^ Taking a step back and thinking about this pattern across the many Rails apps I've seen it in

---

# [fit] Missing<br>Abstraction

^ This just screams missing abstraction!

^ Luckily, we think we've found the abstraction:

---

# [fit] ActionView::Component

^ ActionView::Component!

---

# [fit] ~~ViewModels~~

^ Our current experiment is seeing if we can replace view models with components

^ and so far the results have been very encouraging

---

![fit](img/repo-list-item.png)

^ The first migration we did was creating a component for a repository list item,

^ Which we had implemented almost the exact same way a half dozen places in the app, some of them using view models.

^ Now we have one implementation.

---

^ PAUSE

---

# [fit] The Future

^ So what's next?

---

# [fit] Upstreaming

^ We've already started to upstream our work on components into Rails.

^ After sharing our project at RailsConf in April

^ Rafael from the Rails core team asked us to upstream it into the alpha branch of Rails 6.1

---

`action_view/helpers/rendering_helper.rb`

[.code-highlight: all]
[.code-highlight: 12]
[.code-highlight: 13]

```ruby
def render(options = {}, locals = {}, &block)
  case options
  when Hash
    in_rendering_context(options) do |renderer|
      if block_given?
        view_renderer.render_partial(self, options.merge(partial: options[:layout]), &block)
      else
        view_renderer.render(self, options)
      end
    end
  else
    if options.respond_to?(:render_in)
      options.render_in(self, &block)
    else
      view_renderer.render_partial(self, partial: options, locals: locals, &block)
    end
  end
end
```

^ Our patch updated the render helper method,

^ adding support for passing in an object

^ S that responds\_to `render_in`

^ S if so, `render_in` is called on the object, with the current view context and the passed block as arguments

^ Effectively upstreaming our monkey patch.

^ Our plan is to continue to upstream more of our implementation as it stabilizes internally.

^ PAUSE

---

# [fit] Creativity

^ Creativity is the ability

---

# [fit] Imagine

^ to imagine something new.

^ It is not the ability to create

---

# [fit] Something

^ Something out of

---

# [fit] Nothing

^ Nothing, but to generate

---

# [fit] New ideas

^ New ideas by

---

# [fit] Combining

^ Combining,

---

# [fit] Changing

^ Changing,

---

# [fit] Reapplying

^ or reapplying

---

# [fit] Existing Ideas

^ existing ideas.

---

![50%](img/react.png)

^ By taking ideas from React

---

![50%](img/rails.png)

^ And incorporating them into Rails,

^ We've taken a template that

---

# [fit] Testing

^ Was hard to test efficiently

---

# [fit] Code<br>Coverage

^ Was impossible to audit with code coverage tools

---

# [fit] Data Flow

^ Made it difficult to reason about data flow

---

# [fit] Standards

^ and failed basic Ruby code standards

---

# [fit] ActionView::Component

^ And created a new way of thinking about the view Layer in Rails

^ that enables us to

---

# [fit] Testing

^ Write efficient, isolated tests

---

# [fit] Code<br>Coverage

^ that are audited with code coverage tools

---

# [fit] Data Flow

^ Only work with the values we need

---

# [fit] Standards

^ And follow the code standards of the Ruby language

---

# [fit] MvC

^ All of these things give us higher confidence in our view layer,

^ And perhaps most importantly,

---

# [fit] MVC

^ make it a first class citizen in Rails.

---

# [fit] Thanks

^ Thanks

---

# [fit] Q & A

## [fit] Slides & source code: hawksley.org

^ Repeat questions
