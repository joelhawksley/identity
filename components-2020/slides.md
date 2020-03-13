autoscale: true
slidenumbers: true
theme: Simple, 1
text: Avenir Next Medium, #24292e
text-strong: Avenir Next Bold, #24292e
header: Avenir Next Medium, #24292e
header-strong: Avenir Next Bold, #24292e
code: Menlo Regular, #6f42c1, #005cc5, #0366d6, #d73a49, #d73a49
background-color: #fffcf5;

^ Lots of pauses in hook/intro/thankfulness

^ Servants' mindset

^ YOU GOT THIS

---

# Encapsulating Views

---

# Hi

^ introduce myself

^ name

---

![100%](img/github.png)

^ engineer at on Design Systems team

^ today

^ talk about project

^ working on for the past year

---

# ViewComponent

^ called ViewComponent

---

# Why

^ Why we built it

---

# Lessons

^ lessons learned

---

# Future

^ vision

^ future of rails views at github

---

^ PAUSE

---

[.background-color: #000000]

![fit](img/family.jpg)

^ south of boulder

---

[.background-color: #000000]

![fit](img/sports.jpg)

^ recovering photographer

---

[.background-color: #000000]

![fit](img/portfolio1.jpeg)

^ traveled the country

---

[.background-color: #000000]

![fit](img/portrait.jpg)

^ portraits

---

[.background-color: #000000]

![fit](img/nascar.jpg)

^ every sport you can imagine

---

[.background-color: #000000]

![fit](img/gr.jpeg)

^ worked at newspapers

^ daily life

---

[.background-color: #000000]

![fit](img/si.jpg)

^ breaking news

---

[.background-color: #000000]

![fit](img/biking.jpg)

^ until one day in 2013

^ september 11th

^ out biking

^ friend bryce

^ got a call

^ photo editor, boss laid off

^ her birthday

^ aspired to have her job

^ saw the future of career vanish

^ called Aaron

^ asked for advice

^ gave me better than advice

^ apprenticeship offer

---

[.background-color: #000000]

![fit](img/mojo2.jpg)

^ tiny 8x8 room

^ poor ventilation

^ long days

^ couple of months

^ taught me git, ruby, rails, js

^ how to be a professional engineer

^ wouldn't be be here if it wasn't for him

^ enough about me

---

^ PAUSE

---

# Thanks

^ stressful times

^ therapist encourages focusing on gratitude

^ reflecting on what I'm thankful for

---

# Time

^ Thankful for your time

^ Precious resource

---

# Clarity

^ It's a source of clarity in my life

^ Realize how finite our time here is

^ motivated to use time in a way that matters

---

> "We’re tight-fisted with property and money, yet think too little of wasting time, the one thing about which we should all be the toughest misers."
-- SENECA, ON THE SHORTNESS OF LIFE, 3.1–2

^ Read quote

---

^ Thank you for your time today

^ It is valuable

^ It is precious

^ PAUSE

---

# You

^ You make it special to work here

^ You make it feel like family

---

# Thanks

^ We have something special here

^ So thankful for it

---

^ PAUSE

---

# Thanks

^ also thankful

---

# Rails

^ for rails

^ around a long time

^ think about how much Rails has enabled us all to accomplish

^ that's something to be thankful for

---

# Value

^ value Rails has brought to the world

^ Rails has enabled us to focus on the needs of the people who use our products

^ value comes from what we don't have to worry about any more

^ Not just CSRF protection

---

# Rails @ GitHub

^ Rails is a big part of GitHub's success

---

# >800 contributers

^ More than 800 contributors last year

---

# Scale

^ Rails has scaled with GitHub

^ App is vanilla Rails

^ Just a lot of Rails

----

# >700 models

^ Over 700 models

---

# >600 controllers

^ Over 600 controllers

---

# >4,200 views

^ Over 4,200 views

^ and it's this part of our scale that I'm going to focus on

---

^ PAUSE

---

# A View Problems

^ seen scaling issues before

^ here are a few examples of what they've looked like

---

# Decorators

^ First time I saw it

^ First job, a consultancy

^ After working on a couple Rails projects

^ Landed on a bigger app

^ First time I saw a Rails folder that didn't belong

^ Felt weird

^ Didn't know whether I should be OK with it

^ Model-specific view logic

---

```ruby
class UserDecorator < Draper::Decorator
  delegate_all

  def status
    if active?
      "Last active at #{last_active_at}"
    else
      "Inactive"
    end
  end
end
```

^ Looked like this

^ talk through code

^ place to put view-related logic for a specific model

^ really just another place to hide methods

^ unit tested like models

---

# react_rails

^ Second example

^ Using React to build UI

^ Could have server rendered

^ But used react because of unit tests

---

```erb
<%= react_component("Button", { label: "Open" }) %>
```

```jsx
it('should render the button', function() {
  expect(shallow(<Button props={{ label: "Open" }} />).
  contains(<div className="Button">Open</div>)).toBe(true);
});
```

^ Looked like this

^ tests were written in js

^ super fast

---

# Presenters

^ A third example

^ Folder called presenters

^ also called view models

^ View-specific logic

^ Extracted to Ruby objects

---

```ruby
class RepositoryIndexView < ViewModel
  def status
    repository.locked? ? "Disabled" : "Enabled"
  end
end

class RepositoryIndexViewTest < GitHub::TestCase
  context "#status" do
    test "enabled for unlocked repository" do
      file_view = RepositoryIndexView.new(repository: create(:repository))

      assert_equal file_view.status, "Enabled"
    end

    # ...
  end
end
```

^ looked like this

^ coupled to a specific view

^ easier to test

^ distraction, not really testing the view

---

# Logic-filled partials

^ Fourth example

^ app that had lots of logic in partials

^ simplified logic - in one place

^ but was hard to test

---

```erb
<% status = repository.locked? ? "Disabled" : "Enabled" %>

<h2><%= status %></h2>
```

^ looked like this

^ ended up with view files with ruby blocks dozens of lines long

---

`# app/views/billing_settings/_github_packages_section.html.erb`

```erb
<%
usage = Billing::Usage.new(view.account)
unit_cost = BigDecimal(::Billing::Product::UNIT_COST)
included_usage = [usage.paid_gigabytes, usage.plan_bandwidth].min
usage_cost = view.pricing.downloads_cost
transfer_group = OpenStruct.new(
  transfer_type: "Data transfer out",
  breakdown: [
    OpenStruct.new(
      name: "Data transfer out (rounded)",
    )
  ]
)
%>
```

---

^ PAUSE

^ that's what I've seen

^ what about the rest of the ecosystem

---

# Other apps

^ local ruby group to share app folders

---

![fit](img/app-folders/2-highlighted.png)![fit](img/app-folders/6-highlighted.png)

^ sometimes decorators

---

![fit](img/app-folders/4-highlighted.png)![fit](img/app-folders/7-highlighted.png)![fit](img/app-folders/8-highlighted.png)![fit](img/app-folders/9-highlighted.png)

^ sometimes presenters

---

![fit](img/app-folders/3-highlighted.png)![fit](img/app-folders/10-highlighted.png)![fit](img/app-folders/5-highlighted.png)![fit](img/app-folders/11-highlighted.png)

^ sometimes more than once!

---

# >50%

^ More than half of the responses

^ had view related abstractions

^ not provided by Rails

^ every big app I've worked in has used one

^ can also see the trend in the rails ecosystem

---

# Gems

^ Some popular gems for these patterns

---

# Draper & Cells

^ Draper and Cells have millions of downloads

^ PAUSE

---

# Something's missing.

^ It's clear

^ Something is missing here

---

# Why?

^ why do we turn to these abstractions?

^ Why are we breaking from rails convention?

^ in talking with many of you

---

# Testing

^ comes down to testing

---

# Testing views

^ Why aren't views easy to test?

---

![fit](img/test-pyramid.png)

^ Martin fowler's test pyramid

^ illustrates it best

^ explain chart levels

^ Rails provides

^ controller tests (service)

^ UI tests (system)

^ But not unit tests...

---

![fit](img/test-pyramid-highlighted.png)

^ Limiting us to

^ Slowest and most expensive options

^ As our apps grow

---

# View objects

^ Turn to view objects

^ Can be unit tested

^ enabling thorough coverage

^ without high cost of controller or system tests

---

^ PAUSE

^ Even if our views could be unit tested

^ points to a bigger issue:

---

# Encapsulation

^ Encapsulation

^ What is it?

^ according to the fountain of knowledge wikipedia

---

> "In object-oriented programming, encapsulation refers to the **bundling of data with methods** that operate on that data, or the **restricting of direct access** to some of an object's components."

^ read quote

^ bundling of data

^ restricting of access

^ encapsulation is a fundamental aspect of OO

---

# Encapsulation in Rails

^ rails does provide encapsulation

^ some of the time

---

# Models

^ models are encapsulated

---

[.code-highlight: 1]
[.code-highlight: 1, 4-6]
[.code-highlight: 1,2, 8-12]

```ruby
class User < ApplicationRecord
  after_create :send_welcome_email

  def name
    "#{first_name} #{last_name}"
  end

  private

  def send_welcome_email
    UserMailer.welcome(self)
  end
end
```

^ user model

^ S name method is bundling

^ S welcome email callback is private

^ restricted from direct access

---

`# test/models/user_test.rb`

```ruby
assert_equal(user.name, "Rylan Bowers")
```

^ Test against public interface

^ but not against private methods

---

# Controllers

^ rails controllers are also encapsulated

---

[.code-highlight: 1]
[.code-highlight: 1, 2-4]
[.code-highlight: 1, 6-10]

```ruby
class UsersController < ApplicationController
  def show
    render("users/show", current_user: current_user)
  end

  private

  def current_user
    User.find(params[:id])
  end
end
```

^ users controller

^ S show method is bundling

^ S private current user method

^ restricted from direct access

---

`# test/controllers/users_controller_test.rb`

```ruby
get :show

assert_includes response.body "Rylan Bowers"
```

^ slightly less direct, but interfaces with show

^ does not test current_user method directly

---

# Views

^ what about views?

---

```erb
<% status = repository.locked? ? "Disabled" : "Enabled" %>

<h2><%= status %></h2>
```

^ closest thing to encapsulation is local variable assignment

^ as for testing

---

# ~~interface~~

^ no public interface for views

^ we can't really unit test them

^ To see why encapsulation of views is an issue

^ we need to understand how they work

^ PAUSE

---

# What _are_ views?

^ what are views?

---

# ~~Objects~~

^ Unlike models and controllers

^ they aren't objects

^ PAUSE

^ So let's look at an example

---

<!-- TODO code highlighting -->

`# app/views/demo/index.html.erb`

```erb
<% @message = "Hello World" %>
<%= render(partial: "message", locals: { class_names: "greeting" }) %>
```

<br />
`# app/views/demo/_message.html.erb`

```erb
<h1 class="<%= class_names %>"><%= @message %></h1>
```

^ Deep dive

^ Explicit render of a partial from another file

^ Example code

^ Two views

^ anyone want to guess what happens?

---

![inline](img/helloworld.png)

^ Result

---

```erb
<%= render(...) %>
```

^ What happens when that method is called

^ A lot happens

^ More interesting part

---

`# ActionView::Template`

[.code-highlight: 1]
[.code-highlight: 3]


```ruby
def render(view, locals, buffer = ActionView::OutputBuffer.new, &block)
  instrument_render_template do
    compile!(view)
    view._run(method_name, self, locals, buffer, &block)
  end
rescue => e
  handle_render_error(view, e)
end
```

^ Arguments

^ S compile step

---

[.code-highlight: 0]
[.code-highlight: 1-3]
[.code-highlight: 18]
[.code-highlight: 15, 18]

`# ActionView::Template`

```ruby
# Compile a template. This method ensures a template is compiled
# just once and removes the source after it is compiled.
def compile!(view)
  return if @compiled

  # Templates can be used concurrently in threaded environments
  # so compilation and any instance variable modification must
  # be synchronized
  @compile_mutex.synchronize do
    # Any thread holding this lock will be compiling the template needed
    # by the threads waiting. So re-check the @compiled flag to avoid
    # re-compilation
    return if @compiled

    mod = view.compiled_method_container

    instrument("!compile_template") do
      compile(mod)
    end

    @compiled = true
  end
end
```

^ blank

^ S comment

^ S compile

^ S method container

^ method container is the ActionView::Base class

^ PAUSE

---

[.code-highlight: 1]
[.code-highlight: 3]

`# ActionView::Template`

```ruby
def compile(mod)
  source = encode!
  code = @handler.call(self, source)

  source = +<<-end_src
    def #{method_name}(local_assigns, output_buffer)
      @virtual_path = #{@virtual_path.inspect};#{locals_code};#{code}
    end
  end_src

  mod.module_eval(source, identifier, 0)
end
```

^ Non bang compile method

^ S interesting line is handler.call

---

[.code-highlight: 0]
[.code-highlight: 1]
[.code-highlight: 1, 3-4]
[.code-highlight: 1, 6-7]
[.code-highlight: 1, 9-10]
[.code-highlight: 1, 12-14]

`# ActionView::Template`

```ruby
code = @handler.call(self, source)

irb> @handler
=> #<ActionView::Template::Handlers::ERB:0x00007fb57e348740>

irb> self
=> #<ActionView::Template app/views/demo/_message.html.erb locals=[]>

irb> source
=> "<h1><%= @message %></h1>"

irb> @handler.call(self, source)
=> "@output_buffer.safe_append='<h1>'.freeze;@output_buffer.append=( @message );
   @output_buffer.safe_append='</h1>'.freeze;\n@output_buffer.to_s"
```

^ go through steps

^ output is ruby code

---

`# @handler.call`

```ruby
@output_buffer.safe_append='<h1>'.freeze;
@output_buffer.append=( @message );
@output_buffer.safe_append='</h1>'.freeze;
@output_buffer.to_s
```

<br />

`# _message.html.erb`

```erb
<h1><%= @message %></h1>
```

^ turned ERB into Ruby

---

[.code-highlight: 0]
[.code-highlight: 3]
[.code-highlight: 5-9]

`# ActionView::Template`

```ruby
def compile(mod)
  source = encode!
  code = @handler.call(self, source)

  source = +<<-end_src
    def #{method_name}(local_assigns, output_buffer)
      @virtual_path = #{@virtual_path.inspect};#{locals_code};#{code}
    end
  end_src

  mod.module_eval(source, identifier, 0)
end
```

^ so back in actionview template

^ S we've compiled our template into ruby code

^ S and now let's use it to define a method

---

[.code-highlight: 1-5]
[.code-highlight: 1-5, 7-8]
[.code-highlight: 1-5, 10-11]
[.code-highlight: 1-5, 13-15]

`# ActionView::Template`

```ruby
source = +<<-end_src
  def #{method_name}(local_assigns, output_buffer)
    @virtual_path = #{@virtual_path.inspect};#{locals_code};#{code}
  end
end_src

irb> method_name
=> "_app_views_demo__message_html_erb__3147936528918386365_70191870416280"

irb> @virtual_path.inspect
=> "demo/_message"

irb> code
=> "@output_buffer.safe_append='<h1>'.freeze;@output_buffer.append=( @message );
   @output_buffer.safe_append='</h1>'.freeze;\n@output_buffer.to_s"
```

^ inspect current state

^ generating this ruby:

---

[.code-highlight: 1]
[.code-highlight: 1-7]

```ruby
def _app_views_demo__message_html_erb__3026934259175371146_70158375537500(local_assigns, output_buffer)
  @virtual_path = "demo/_message"
  @output_buffer.safe_append='<h1>'.freeze
  @output_buffer.append=( @message )
  @output_buffer.safe_append='</h1>'.freeze
  @output_buffer.to_s
end
```

^ This method

^ generated name

^ body generated by the handler

---

[.code-highlight: all]
[.code-highlight: 11]

`# ActionView::Template`

```ruby
def compile(mod)
  source = encode!
  code = @handler.call(self, source)

  source = +<<-end_src
    def #{method_name}(local_assigns, output_buffer)
      @virtual_path = #{@virtual_path.inspect};#{locals_code};#{code}
    end
  end_src

  mod.module_eval(source, identifier, 0)
end
```

^ blank

^ S attach to compiled method container

---

```ruby
irb> self.methods...
=> [
  :_app_views_demo_index_html_erb__1824471460578655455_70348614451620
  :_app_views_demo__message_html_erb__1856726472418298868_70348613288120,
  :_app_views_layouts_application_html_erb__3293958388228102565_70348615263920,
]
```

^ Container contents

---

[.code-highlight: 0]
[.code-highlight: 3]
[.code-highlight: 4]
[.code-highlight: 1,4]
[.code-highlight: 1,4, 10,11]
[.code-highlight: 1,4, 13,14]
[.code-highlight: 1,4, 16,17]

`# ActionView::Template`

```ruby
def render(view, locals, buffer = ActionView::OutputBuffer.new, &block)
  instrument_render_template do
    compile!(view)
    view._run(method_name, self, locals, buffer, &block)
  end
rescue => e
  handle_render_error(view, e)
end

irb> method_name
=> "_app_views_demo__message_html_erb___1878705374794196717_70220992442400"

irb> self
=> #<ActionView::Template app/views/demo/_message.html.erb locals=[]>

irb> buffer.class
=> ActionView::OutputBuffer
```

^ end of the road

^ S Compiled

^ S all that's left is to run

^ Closer look at state

^ S method_name

^ S self

^ S output buffer

---

[.code-highlight: 0]
[.code-highlight: 1-3]
[.code-highlight: 4]

`# ActionView::Base`

```ruby
def _run(method, template, locals, buffer, &block)
  @current_template = template
  @output_buffer = buffer
  send(method, locals, buffer, &block)
end
```

^ Really, this is it

^ S set the template and buffer

^ S then call the compiled method we defined above

---

[.code-highlight: 4]

`# ActionView::Base`

```ruby
def _run(method, template, locals, buffer, &block)
  @current_template = template
  @output_buffer = buffer
  _app_views_demo__message_html_erb__3026934259175371146_70158375537500(locals, buffer, &block)
end
```

^ So effectively we end up with this

---

^ And that's the entire call stack

^ for rendering a view

^ I'm guessing you all are thinking:

---

![inline](img/wat.jpg)

^ Wat

---

^ Deep breath

^ What does this all mean?

^ What are the implications?

^ What does this have to do with encapsulation?

^ Isn't that a lot of work?

---

# Views _are_ methods

---

# On the _same_ module

---

# Templates * locals

^ compiled based on local keys

^ Meaning Rails is dynamically generating a method for each combination of

^ a template and the local keys passed to it

---

`# index.html.erb`

```erb
<% @message = "Hello World" %>
<%= render("message") %>
```

<br />
`# _message.html.erb`

```erb
<h1><%= @message %></h1>
```

^ Look at templates

^ run through compilation

---

[.code-highlight: 1,2,7, 9, 15, 16]
[.code-highlight: 2]
[.code-highlight: 2,4]
[.code-highlight: 2,4-5]
[.code-highlight: 9]
[.code-highlight: 9, 12]

```ruby
class ActionView::Base
  def _app_views_demo_index_html_erb___42169053093465020_70319914664120(local_assigns, output_buffer)
    @virtual_path = "demo/index"
    @message = "Hello World"
    @output_buffer.append=( render("message") )
    @output_buffer.to_s
  end

  def _app_views_demo__message_html_erb___154141396804859982_70319911264400(local_assigns, output_buffer)
    @virtual_path = "demo/_message"
    @output_buffer.safe_append='<h1>'.freeze
    @output_buffer.append=( @message )
    @output_buffer.safe_append='</h1>'.freeze
    @output_buffer.to_s
  end
end
```

^ Rails sees this

^ Sibling methods

^ Instance variables across views

^ On ActionView::Base

^ S render index

^ S set message to "Hello world"

^ S then render the "message" partial

^ S calls the generated method for the partial

^ S which has access to the message instance variable

---

# Global scope

^ Global scope explosion

^ All views

^ All helpers

^ Same context

^ Can all share state

---

# Encapsulation

^ not much encapsulation

^ All 4,200-odd views exist in the same scope

^ They aren't going anywhere

---

^ PAUSE

^ What might encapsulated views look like?

---

# Decorators, Presenters, Components

^ Many of us have solutions to make them easier to test

^ Why don't we bring those ideas into Rails?

---

# 2019

^ Spent most of the past year

^ Incorporating those ideas

^ Into a vision for how Rails could address these issues

---

# ViewComponent

^ called ViewComponent

^ incorporates best parts of existing patterns

^ into the Rails architecture

---

# Encapsulation

^ First and foremost

^ ViewComponents are encapsulated

---

# one object for _all_ views

^ instead of one object with all views

---

# one object _per_ view

^ one object *per* view

---

`# app/components/message_component.rb`

```ruby
class MessageComponent < ViewComponent::Base
  def initialize(message:)
    @message = message
  end
end
```

`# app/components/message_component.html.erb`

```erb
<h1><%= @message %><h1>
```

`# app/views/demo/index.html.erb`

```erb
<%= render(MessageComponent.new(message: "Hello, World!")) %>
```

^ Take this example

^ two files side by side

^ (talk through code)

---

`# app/views/demo/index.html.erb`

```erb
<%= render(MessageComponent.new(message: "Hello, World!")) %>
```

^ Looking at render call

^ component referenced directly

^ instead of through view method lookup

^ no ambiguity

^ PAUSE

---

`# app/components/message_component.rb`

```ruby
class MessageComponent < ViewComponent::Base
  def initialize(message:)
    @message = message
  end
end
```

`# message_component.html.erb`

```erb
<h1><%= @message %><h1>
```

^ looking back at component

^ Follow a similar compilation process

---

`# app/components/message_component.rb`

```ruby
class MessageComponent < ViewComponent::Base
  def initialize(message:)
    @message = message
  end

  def call
    @output_buffer.safe_append='<h1>'.freeze
    @output_buffer.append=( @message )
    @output_buffer.safe_append='</h1>'.freeze
    @output_buffer.to_s
  end
end
```

^ But instead attach compiled view to component object

^ No access to state from other views

^ No instance variable leakage

---

[.code-highlight: all]
[.code-highlight: 2]

`# app/components/message_component.rb`

```ruby
class MessageComponent < ViewComponent::Base
  include IconHelper

  def initialize(message:)
    @message = message
  end
end
```

`# app/components/message_component.html.erb`

```erb
<h1><%= @message %><h1>
```

^ Also encapsulate access to helpers

^ S can be included in component class, or:

---

[.code-highlight: 16]

`# app/components/message_component.rb`

```ruby
class MessageComponent < ViewComponent::Base
  include IconHelper

  def initialize(message:)
    @message = message
  end
end
```

`# app/components/message_component.html.erb`

```erb
<h1><%= @message %><h1>
<%= helpers.star_icon %>
```

^ or via helpers. method escape hatch

---

# Unit testing

[.code-highlight: all]
[.code-highlight: 3]
[.code-highlight: 3, 5]

```ruby
RSpec.describe BoxComponent do
  it "renders message" do
    render_inline(MessageComponent.new(message: "Hello, World!"))

    assert_text "Hello, World!"
  end
end
```

^ Unit testing components is simple

^ S Render component inline

^ S assert against rendered result

^ Fast

^ We end up writing a lot of them

---

# `gem "actionview-component"`

^ Published in august

^ extraction from GitHub

^ My first open source project

^ blown away by support

^ shipped 20 releases

---

# Contributors

^ most work has come from the community

^ two dozen contributors

^ seven or eight countries

^ Some cool contributions include:

---

> `rails g component Example`
-- Vinicius Stock, Toronto

^ Simple things like

^ Adding generator support

^ Vinicius Stock from Shopify

---

> `Component::Preview`
-- Juan Manuel Ramallo, Argentina

^ More complex feature

^ Component previews

^ Similar to mailer previews

^ Juan Manuel Ramallo from Argentina

---

[.code-highlight: 1,2]
[.code-highlight: 1,2-5]
[.code-highlight: 1,2, 7-9]

```ruby
module Issues
  class BadgeComponentPreview < ViewComponent::Preview
    def open
      render(Issues::BadgeComponent.new(state: :open))
    end

    def closed
      render(Issues::BadgeComponent.new(state: :closed))
    end
  end
end
```

^ Just like with mailers

^ Inherits from preview class

^ Method for each preview

^ S Open

^ S Closed

---

![inline](img/previews.png)

^ simple UI

^ when you click

---

![inline](img/preview.png)

^ renders the component by itself

---

> `with_content_areas`
-- Jon Palmer, Boston

^ feature by Jon Palmer from Boston

---

![fit](img/box-component.png)

^ box component

^ from design system

---

[.code-highlight: all]
[.code-highlight: 2]
[.code-highlight: 3]
[.code-highlight: 4]

```html
<div class="Box">
  <div class="Box-header"><h3 class="Box-title">Box title</h3></div>
  <div class="Box-body">Box body</div>
  <div class="Box-footer">Box footer</div>
</div>
```

^ here is the html

^ S header

^ S body

^ S footer

---

```erb
<div class="Box">
  <div class="Box-header"><h3 class="Box-title">Box title</h3></div>
  <div class="Box-body">Box body</div>
  <div class="Box-footer">Box footer</div>
</div>
```

^ Go back to example HTML

^ rewrite as ViewComponent

---

`# app/components/box_component.rb`

```ruby
class BoxComponent < ViewComponent::Base
  def initialize
  end
end
```

`# app/components/box_component.html.erb`

```erb
<div class="Box">
  <div class="Box-header"><h3 class="Box-title">Box title</h3></div>
  <div class="Box-body">Box body</div>
  <div class="Box-footer">Box footer</div>
</div>
```

`# app/views/demo/index.html.erb`

```erb
<%= render(BoxComponent.new) %>
```

^ start with a component that renders our example code

---

`# app/components/box_component.rb`

```ruby
class BoxComponent < ViewComponent::Base
  def initialize
  end
end
```

`# app/components/box_component.html.erb`

```erb
<div class="Box">
  <%= content %>
</div>
```

`# app/views/demo/index.html.erb`

```erb
<%= render(BoxComponent.new) do %>
  <%= render(BoxHeaderComponent.new) do %>Box title<% end %>
  <%= render(BoxBodyComponent.new) do %>Box body<% end %>
  <%= render(BoxFooterComponent.new) do %>Box footer<% end %>
<% end %>
```

^ look something like this

^ order of elements matters

^ enforce header is first?

^ enforce footer is last?

^ doesn't prevent misuse of the design system

---

`# app/components/box_component.rb`

```ruby
class BoxComponent < ViewComponent::Base
  def initialize
  end
end
```

^ back in component

---

[.code-highlight: 2]

`# app/components/box_component.rb`

```ruby
class BoxComponent < ViewComponent::Base
  with_content_areas :header, :body, :footer

  def initialize
  end
end
```

^ we can declare multiple content areas

---

[.code-highlight: 1-5]
[.code-highlight: 7-11]

`# app/views/demo/index.html.erb`

```erb
<%= render(BoxComponent.new) do %>
  <%= render(BoxHeaderComponent.new) do %>Box title<% end %>
  <%= render(BoxBodyComponent.new) do %>Box body<% end %>
  <%= render(BoxFooterComponent.new) do %>Box footer<% end %>
<% end %>

<%= render(BoxComponent.new) do |component| %>
  <% component.with(:header) do %>Box title<% end %>
  <% component.with(:body) do %>Box body<% end %>
  <% component.with(:footer) do %>Box footer<% end %>
<% end %>
```

^ In template that renders component

^ refactor it

^ S to use named blocks instead of separate components

^ PAUSE

---

[.code-highlight: 1-3]
[.code-highlight: 6]
[.code-highlight: 6-7]
[.code-highlight: 6-8]
[.code-highlight: 5-9]

`# app/components/box_component.html.erb`

```erb
<div class="Box">
  <%= content %>
</div>

<div class="Box">
  <div class="Box-header"><h3 class="Box-title"><%= title %></h3></div>
  <div class="Box-body"><%= body %></div>
  <div class="Box-footer"><%= footer %></div>
</div>
```

^ and then in our component template

^ rewrite it to

^ render the

^ S title

^ S body

^ S and footer

^ S inside wrapping div

^ PAUSE

---

`# app/components/box_component.rb`

```ruby
class BoxComponent < ViewComponent::Base
  with_content_areas :header, :body, :footer

  def initialize
  end
end
```

`# app/components/box_component.html.erb`

```erb
<div class="Box">
  <div class="Box-header"><h3 class="Box-title"><%= title %></h3></div>
  <div class="Box-body"><%= body %></div>
  <div class="Box-footer"><%= footer %></div>
</div>
```

^ ended up with a codification of the design system

---

# component gems

^ another cool thing

^ since components are ruby classes

^ we can extract them into gems

^ we haven't done this yet

^ know of some who have

---

![inline](img/component-gem.png)

^ financial services

^ half dozen apps using a single gem

^ we're planning to do the same

^ PAUSE

---

![inline](img/rails-pr.png)

^ Most exciting

^ landed PRs in rails to support this architecture

^ will be shipping in Rails 6.1 this spring

^ PAUSE

---

# Performance

^ so what about performance?

---

# templates * locals

^ remember how

^ method for each unique locals passed to template at runtime

---

# Caching

^ leads to less than optimal caching behavior

^ Cached at runtime, after forking servers like Unicorn and Puma

^ One part of cold first request render times being slow

^ at our scale, thousands of processes

^ each time process serves a view it hasn't seen before

^ has to compile the view first

^ Rails 6 contained some optimizations by John Hawthorn

^ Templates now cached between requests in dev

^ Internal code in our app with a more extreme optimization

^ Enabled by having linters:

---

# `render("users/index")`

^ Linter to enforce full path

---

```ruby
class RepositoriesController
  def show
    render("repostiories/show")
  end
end
```

^ Linter to enforce explicit render calls in controllers

---

[.build-lists: true]

1. Scan all templates for render calls
1. Group by template
1. Find unique combinations of locals
1. Compile template for each combination

^ Scan

^ S Group

^ S Uniq combinations of locals

^ S Compile for each

^ fortunately components are easier to optimize

---

`# app/components/message_component.rb`
```ruby
class MessageComponent < ViewComponent::Base
  def initialize(message:)
    @message = message
  end

  def call
    @output_buffer.safe_append='<h1>'.freeze
    @output_buffer.append=( @message )
    @output_buffer.safe_append='</h1>'.freeze
    @output_buffer.to_s
  end
end
```

^ example component

^ is compiled before Unicorn and Puma fork

---

# Performance

^ Just the beginning

^ Designed to allow optimization

---

# Migration path

^ If you want to give it a try

^ Easy way is to migrate a view model

^ what we've been doing

^ Linter to cap view model usage, directing to components instead

---

# Tests

^ Immediate testing benefit

^ Migrate unit tests from previous abstraction

^ Also migrate most controller tests

^ can test against output html

^ Might find missing coverage in the process

---

# New views

^ What about for new views

^ While components are useful for building entire views

^ Our rule has been:

---

# "If it could be a partial, it could be a component"

^ "If it could be a partial, it could be a component"

^ encourage to start there

---

## #view-component<br />@github/view-component-reviewers

---

^ PAUSE

---

# The Future

^ what about the future

---

# Rails

^ goal to eventually incorporate into rails

---

^ PAUSE

---

# ~~Secret~~

^ No secret

^ Future of Rails is inside your applications

---

# Progress

^ Frameworks like Rails help us move human progress forward

^ allowing us to focus on new and important problems

^ in a changing world,

---

# It's up to us.

^ up to us to make thoughtful extractions

^ keep Rails relevant

---

# Time

^ Our time is precious

---

# How will you spend yours?

^ How will you spend yours?

---

# Thanks

^ What was confusing? What could I improve?

---