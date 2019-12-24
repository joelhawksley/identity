autoscale: true
slidenumbers: true
theme: Simple, 1
text: Avenir Next Medium, #24292e
text-strong: Avenir Next Bold, #24292e
header: Avenir Next Medium, #24292e
header-strong: Avenir Next Bold, #24292e
code: Menlo Regular, #6f42c1, #005cc5, #0366d6, #d73a49, #d73a49
background-color: #ffffff;

---

^ Set out to collect these ideas and think about what it might look like to bring them into Rails.

---

# How Rails views work today

^ How rails views work today
^ Single module
^ List number of methods defined dynamically on GH app
^ Why this is bad
^ encapsulation

---

# ActionView::Component Prototype

^ What we do is the best:
^ Encapsulating into a single object
^ Easier to make fast
^ Better than partials and helpers
^ Instance variable context encapsulation

---

^ superset of the rails view layer
^ Works exactly as you’d expect it to

---

# Performance

^ Requests per second

^ It works for us

---

# Rails Patch

^ In June, we landed a patch in Rails that added support for `render_in`

^ Support from Rafael

---

# Gem

^ In August, we published version one of the `actionview-component` gem, extracting the library from `github/github`

---

^ Since then, we've shipped X releases

---

^ With a large majority of contributions coming from the Rails community

---

^ Blown away by support

^ My first open source project

^ We've added a bunch of features

---

# Generators

^ Kasper ?

---

# Previews

^ Juan Manuel Ramallo

---

^ Similar to ActionMailer::Previews

---

---

# Lessons of the past year

---

## Migration path

^ “If it could be a partial, it could be a good component”

---

# Thanks

^ Slide of all contributors
