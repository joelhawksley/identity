autoscale: true
slidenumbers: true
slidecount: true
footer: hawksley.org/components

# [fit] Rethinking the View Layer <br> with Components

^
Thanks to the RailsConf organizers
Excited to be giving first conference talk

---

# Joel Hawksley
## hawksley.org

^ My name is Joel.
I live in Colorado.

---

![40%](img/github.png)

^
Engineer at GitHub

---

^
Learning new languages and frameworks
Give us a new way of thinking about the world

---

![50%](img/react.png)

^ Especially true for me with React

---

# [fit] Rethinking the View Layer <br> with Components

^
Changed the way I look at Rails
Going to talk about that change in perspective

---

```erb
<% if pull && pull.merged? %>
  <div class="State State--purple">
    <%= octicon('git-merge') %> Merged
  </div>
<% elsif pull && pull.closed? %>
  <div class="State State--red">
    <%= octicon('git-pull-request') %> Closed
  </div>
<% elsif pull %>
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

^
- Do this through an exercise
- Take template from the GitHub app
- Is hard to test efficiently
- Is impossible to measure with code coverage tools
- Overfetches ActiveRecord objects
- Fails basic Ruby code standards

---

```erb
<%= render Issues::Badge, is_pull: true, state: :merged %>
```

^
- Refactor into Ruby classes
- Are tested efficiently, in isolation
- Are audited using code coverage tools
- Only receive the data they need
- Follow the code standards of the Ruby language
- And perhaps most importantly

---

# [fit] >100x

^
Are over 100x faster to test

---

# [fit] Views

^
- What even is a view?
- Helpful to have a definition

---

# [fit] Data -> HTML

^
- Views are programs
- They input (data), and return an output, HTML.
- Rails over the years?

---

# [fit] 2004 **ERB 1.0**
# [fit] 2005 **Rails 1.0**
# [fit] 2012 **Turbolinks**
# [fit] 2016 **API Mode**

^
- Things haven’t changed much
- Rails still using embedded ruby templates
- Rails 4 partial page reloads with Turbolinks
- And Rails 5 API mode

---

> "Rails is not only a great choice when you want to build a full-stack application that uses server-side rendering of HTML templates, but also a great companion for the new crop of client-side JavaScript or native applications that just needs the backend to speak JSON."
-- DHH

^
DHH said in the announcement of Rails 5

---

# [fit] 2004 **ERB 1.0**
# [fit] 2005 **Rails 1.0**
# [fit] 2012 **Turbolinks**
# [fit] 2016 **API Mode**

^
- The history of the Rails view layer is one of most of us moving away from it

---

![40%](img/github.png)

^
- So what does the view layer look like at GitHub?

---

# [fit] ERB

^
- Still using embedded ruby
- Why isn’t GitHub a single page app like everything else these days?

---

# [fit] Progressive <br> Enhancement

- Progressive enhancement.
- GitHub is built to be usable without Javascript enabled.
- It’s easy to forget about users in developing countries
- Low powered netbooks, chrome books, or tablets, which buckle under heavy Javascript.
- Allows graceful fallback support for older browsers

---

[.code-highlight: all]
[.code-highlight: 3-6]
[.code-highlight: 2-6]
[.code-highlight: 8]
[.code-highlight: all]

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

^
- How do we do it?
- Couple tiers of Javascript bundles
- Fully supported browsers -> normal bundles.
- Polyfills to second tier that need it.
- Unsupported -> ONLY smaller set of polyfills
- Deprecate browsers -> tiers of support

---

# [fit] Server <br> Rendering

^
All rendering on the server

---

[.hide-footer]

![fit](img/pjax.png)

^
- New issue comment
- JS intercepts click
- AJAX request returns DOM nodes for sidebar, comment form, timeline
- Inject results into page
- Using PJAX, like Turbolinks
- Javascript turned off -> normal page request and reload
- PAUSE

---

![40%](img/github.png)

^
- Let’s talk about building views at GitHub

---

[.hide-footer]
[.slidenumbers: false]
[.slidecount: false]

![fit](img/sticky.gif)

^
- Project paper cuts
- Make GitHub better through incorporating community feedback
- Over a hundred releases in the past year
- Recently shipped sticky headers

---

![fit](img/issue-status-highlight.png)

^
- This is the issue badge
- Display the status of Issues and PRs

---

# [fit] Issue
# [fit] belongs_to:
# [fit] PullRequest

^
- In GitHub data model
- PR is just an issue with an associated PullRequest object.

---

```erb
<% if pull && pull.merged? %>
  <div class="State State--purple">
    <%= octicon('git-merge') %> Merged
  </div>
<% elsif pull && pull.closed? %>
  <div class="State State--red">
    <%= octicon('git-pull-request') %> Closed
  </div>
<% elsif pull %>
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

^
- Shared issue badge partial
- Renders icon, label, color
- State of issue or PR
- PAUSE
- Reuse for sticky headers
- Only found a single happy path controller test
- Not right

---

```bash

$ ls -1 github/app/models | wc -l
556

$ find github/app/views -print | wc -l
3718

$ ls -1 github/app/controllers | wc -l
209
```

^
- Not so simple at GitHub
- 10-year-old Rails monolith
- 500 models
- 3700 views
- 200 controllers
- Not including API
- PAUSE
- Affect approach to testing views?

---

# [fit] 6s
### (GET + assert)

^
- Six second for single controller test
- One minute for suite of ten tests just to get feedback

---

^

- So you know when you’re at an event and they have a minute of silence?
- Imagine that, every time you make a change.
- DRAMATIC PAUSE
- Ok, you get the point


---

#[fit] ?

^
- So why isn’t testing our views thoroughly a more common practice?
- PAUSE
