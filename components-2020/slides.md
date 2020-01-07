autoscale: true
slidenumbers: true
theme: Simple, 1
text: Avenir Next Medium, #24292e
text-strong: Avenir Next Bold, #24292e
header: Avenir Next Medium, #24292e
header-strong: Avenir Next Bold, #24292e
code: Menlo Regular, #6f42c1, #005cc5, #0366d6, #d73a49, #d73a49
background-color: #ffffff;

^ Lots of pauses in hook/intro/thankfulness

^ YOU GOT THIS

---

# I have a secret

^ have a secret to share

---

# The future of Rails

^ future of rails

^ already here

^ already exists

---

# It's in your applications

^ in your apps

---

# It's in your gems

^ in your gems

^ but it won't be the future

^ unless you share it with the rest of us

---

^ PAUSE

---

# Rails

^ rails

^ around for a long time

---

# 2005

^ since 2005

^ eternity in internet time

---

# Relevance

^ And yet it has remained relevant

^ not by accident

---

# Evolution

^ Rails has evolved

^ through features

^ and fixes

^ extracted from other Rails applications

---

# Extraction

^ today

^ talk about extraction

^ from GitHub

^ working on for the past year

---

# ActionView::Component

^ called ActionView Component

---

# Why

^ Why we built it

---

# Lessons

^ lessons learned

---

# Future

^ vision 

^ future of rails views

---

^ PAUSE

---

# Hi

^ introduce myself

^ name

---

![50%](img/microsoft.png)

^ engineer at GitHub

---

![100%](img/github.png)

---

[.background-color: #000000]

![fill](img/earth.jpeg)

^ fully distributed

^ most engineers remote

---

[.background-color: #000000]

![fit](img/family.jpg)

^ south of boulder

^ work from home

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

![fit](img/sports2.jpg)

^ sports

^ did for a little while

---

[.background-color: #000000]

![fit](img/biking.jpg)

^ until one day in 2013

^ out biking

^ friend bryce

^ got a call

^ photo editor, boss laid off

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

^ taught me git, ruby, rails, js

^ how to be a professional engineer

^ wouldn't be be here if it wasn't for him

^ enough about me

---

^ PAUSE

---

# Thanks

^ time of year

^ reflecting on what I'm thankful for

---

# Time

^ Thankful for your time

^ Precious resource

---

![fit](img/prakash.png)

^ Recently lost prakash

^ lost a member of our community

^ Could have been any of us

^ Crazy to think

^ 47 

^ Left behind daughter and wife

---

# Loss

^ Prakash fifth person lost in the past year or so

^ It's been a struggle for me

^ Dark times

---

# Clarity

^ But it's also been a source of clarity in my life

^ Realize how finite our time here is

^ motivated to use time in a way that matters

---

> "We’re tight-fisted with property and money, yet think too little of wasting time, the one thing about which we should all be the toughest misers."
-- SENECA, ON THE SHORTNESS OF LIFE, 3.1–2

^ Read quote

---

^ Thank you for spending time with us

^ It is valuable

^ It is precious

^ PAUSE

---

# Community

^ for our community

^ over a decade

^ almost as old as rails

---

# Sponsors

^ Sponsors

^ Food

^ Drinks

^ Place to meet

^ Sandi Metz fund

---

# Organizers

^ Organizers

^ Dan, Rylan, Marty

^ Those who have helped over the years

^ It wouldn't be possible it without them 

---

# You

^ You make it special

^ You make it feel like family

---

# Thanks

^ We have something special

^ So good I'd still come if it was a javascript meetup

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

^ Not just CSRF protection

---

# Rails @ GitHub

^ Rails is a big part of GitHub's success

---

# Monolith

^ Still a monolith

^ Moving back into monolith

^ as of a year ago 

---

# $7.5 Billon Monolith

^ Now $7.5 billion monolith

^ Has the best name ever

---

# github.com/github/github

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

---

# 12 years old

^ Codebase is about 12 years old

---

# >800 contributers

^ More than 800 contributors last year

---

^ PAUSE

---

# Rails @ GitHub

^ often asked about working on the monolith at GitHub

^ different mindset I noticed when I joined

^ remember Eileen saying

---

> "If it doesn't have to do with our business, it needs to go in Rails."

^ If it doesn't have to do with our business, it needs to go in Rails.

^ In other words

---

# Upstream by default

^ our approach should be to upstream by default

^ not always this way

---

# Forks

^ On fork until 2018

^ Inventing features before Rails

^ unsustainable maintenance

^ backport security fixes

^ hard to onboard

^ Eileen led team for two years

^ got us from a fork of 3.2 to master

^ many benefits

^ but the most critical was

---

# master

^ run a couple weeks behind master 

^ many benefits

^ enabled easy contribution to Rails

^ short lag in between rails and monolith

^ enabled extraction

^ around 100 PRs from GitHub into Rails 6

---

> The best frameworks are in my opinion extracted, not envisioned. And the best way to extract is first to actually do.[^1]
-- DHH

[^1]: https://dhh.dk/posts/6-why-theres-no-rails-inc.html

^ DHH said it best in 2007

---

^ PAUSE

---

# The extraction I couldn't ignore

^ Story

^ extraction

^ Too obvious to ignore

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

^ place to put view-related logic for a specific model

^ really just another place to hide methods

^ unit tested like models

---

# react_rails

^ Second time

^ Using React to build UI

^ Could have server rendered

^ But used react because of unit tests

---

```erb
<%= react_component("Button", { label: "Open" }) %>
```

^ Looked like this

^ tests were written in js

---

# Presenters

^ Third time

^ Folder called presenters

^ View-specific logic

^ Extracted to Ruby objects

---

```ruby
class RepositoryIndexViewModel < ViewModel
  def status
    repository.locked? ? "Disabled" : "Enabled"
  end
end
```

^ looked like this

^ coupled to a specific view

^ easier to test

^ distraction, not really testing the view

---

# Logic-filled partials

^ Fourth time

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

# Components

^ all the while


^ Rise of view components

^ Design systems

^ Open source like bootstrap

^ Internal like Primer at GitHub

---

^ PAUSE

^ that's what I've seen

^ what about you?

---

# Your apps

^ asked to share your app folder

^ wanted to see if it was in your apps too

^ and it was!

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

^ Bigger issue:

---

# Encapsulation

^ Encapsulation

^ What is it?

^ according to the fountain of knowledge wikipedia

---

> "In object-oriented programming, encapsulation refers to the *bundling of data with the methods that operate on that data*, or the *restricting of direct access* to some of an object's components."

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

[.code-higlight: 1]
[.code-higlight: 1, 4-6]
[.code-higlight: 1,2, 8-12]

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
<% status = user.active? "Active" : "inactive" %>

<h1><%= status %></h1>
```

^ closest thing is local variable assignment

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

---

![fit](img/lightspeed.jpg)

^ Adventure

^ wallpapersafari.com

---

^ Lots of ways to render

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

^ Deep dive

^ Explicit render of a partial from another file

^ Example code

^ Two views

^ anyone want to guess what happens?

---

![inline](img/helloworld.png)

^ Result

---

![inline](img/wat.jpg)

^ Wat

---

```erb
<%= render("message") %>
```

^ Journey

---

[.code-highlight: 0]
[.code-highlight: 1]
[.code-highlight: 15]

`# ActionView::Helpers::RenderingHelper`

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

^ First stop on journey

^ S Arguments

^ S End up calling

---

[.code-highlight: 1]
[.code-highlight: 1, 3-4]
[.code-highlight: 1, 6-7]
[.code-highlight: 1, 9-10]


```ruby
view_renderer.render_partial(self, partial: options ...)

irb> view_renderer.class
=> ActionView::Renderer

irb> self.class
=> #<Class:0x00007fea31296760>

irb> options
=> "message"
```

^ What's going on

^ S View renderer

^ S Self is current view

^ S Options is our template name

^ call passes through to

---

`# ActionView::Renderer`

```ruby
def render_partial_to_object(context, options, &block)
  PartialRenderer.new(@lookup_context).render(context, options, block)
end
```

^ action view render, which builds a call to partial renderer

---

[.code-highlight: 1-3]
[.code-highlight: 1-3, 5-6]
[.code-highlight: 1-3, 8-9]
[.code-highlight: 1-3, 11-12]
[.code-highlight: 1-3, 14-15]
[.code-highlight: 1-3, 17-18]

`# ActionView::Renderer`

```ruby
def render_partial_to_object(context, options, &block)
  PartialRenderer.new(@lookup_context).render(context, options, block)
end

irb> @lookup_context.class
=> ActionView::LookupContext

irb> @lookup_context.instance_variable_get(:@details)
=> {:locale=>[:en], :formats=>[:html], :variants=>[], :handlers=>[:raw, :erb, :html, ...]}

irb> @lookup_context.instance_variable_get(:@view_paths).class
=> ActionView::PathSet

irb> context.class
=> #<Class:0x00007fa618132368>

irb> options
=> {:partial=>"message", :locals=>{}}
```

^ look at the state

---

[.code-highlight: 0]
[.code-highlight: 1]
[.code-highlight: 12]
[.code-highlight: 10,12]

`# ActionView::PartialRenderer`

```ruby
def render(context, options, block)
  as = as_variable(options)
  setup(context, options, as, block)

  if @path
    if @has_object || @collection
      @variable, @variable_counter, @variable_iteration = retrieve_variable(@path, as)
      @template_keys = retrieve_template_keys(@variable)
    else
      @template_keys = @locals.keys
    end
    template = find_template(@path, @template_keys)
    @variable ||= template.variable
  else
    if options[:cached]
      raise NotImplementedError, "render caching requires a template. Please specify a partial when rendering"
    end
    template = nil
  end

  if @collection
    render_collection(context, template)
  else
    render_partial(context, template)
  end
end
```

^ S arguments

^ Context is view

^ Options is our partial name

^ S Interesting bit is find_template

^ S based on path and keys of locals

---

[.code-highlight: 1-2]
[.code-highlight: 1-2, 4,5]
[.code-highlight: 1-2, 7,8]
[.code-highlight: 1-2, 10,11]

`# ActionView::PartialRenderer`

```ruby
@template_keys = @locals.keys
template = find_template(@path, @template_keys)

irb> @path
=> "message"

irb> @template_keys
=> []

irb> find_template(@path, @template_keys)
=> #<ActionView::Template app/views/demo/_message.html.erb locals=[]>
```

^ Look at those lines

^ S Path

^ S Template keys

^ S Template object

---

[.code-highlight: 0]
[.code-highlight: 24]

`# ActionView::PartialRenderer`

```ruby
def render(context, options, block)
  as = as_variable(options)
  setup(context, options, as, block)

  if @path
    if @has_object || @collection
      @variable, @variable_counter, @variable_iteration = retrieve_variable(@path, as)
      @template_keys = retrieve_template_keys(@variable)
    else
      @template_keys = @locals.keys
    end
    template = find_template(@path, @template_keys)
    @variable ||= template.variable
  else
    if options[:cached]
      raise NotImplementedError, "render caching requires a template. Please specify a partial when rendering"
    end
    template = nil
  end

  if @collection
    render_collection(context, template)
  else
    render_partial(context, template)
  end
end
```

^ Whole method

^ S context and template object

---

[.code-highlight: 1]
[.code-highlight: 13]

`# ActionView::PartialRenderer`

```ruby
def render_partial(view, template)
  instrument(:partial, identifier: template.identifier) do |payload|
    locals, block = @locals, @block
    object, as = @object, @variable

    if !block && (layout = @options[:layout])
      layout = find_template(layout.to_s, @template_keys)
    end

    object = locals[as] if object.nil? # Respect object when object is false
    locals[as] = object if @has_object

    content = template.render(view, locals) do |*name|
      view._layout_for(*name, &block)
    end

    content = layout.render(view, locals) { content } if layout
    payload[:cache_hit] = view.view_renderer.cache_hits[template.virtual_path]
    build_rendered_template(content, template)
  end
end
```

^ Takes arguments

^ S Renders the view inside the template

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
=> "_app_views_demo__messge_html_erb__3147936528918386365_70191870416280"

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

[.code-highlight: 0]
[.code-highlight: 10]

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

`# ActionView::Template`

[.code-highlight: 0]
[.code-highlight: 3]
[.code-highlight: 4]


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

^ end of the road

^ S Compiled

^ S all that's left is to run

---

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

^ Closer look

^ S method_name

^ S self

^ S output buffer

---

[.code-highlight: 0]
[.code-highlight: 1]
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

^ S args

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

---

[.code-highlight: 1,2,7, 9, 15, 16]
[.code-highlight: 2]
[.code-highlight: 2,4]
[.code-highlight: 2,4-5]
[.code-highlight: 9]
[.code-highlight: 9, 12]

```ruby
class MyViews
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

^ So to recap:

---

# Testing

^ Rails views are hard to test

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

# ActionView::Component

^ called ActionView::Component

^ works exactly as you'd expect it to

^ incorporates best parts of existing patterns

^ into the Rails architecture

---

# Encapsulation

^ First and foremost

^ ActionView::Components are encapsulated

---

# one object for _all_ views

^ instead of one object with all views

---

# one object _per_ view

^ one object *per* view

---

`# message_component.rb`

```ruby
class MessageComponent < ActionView::Component::Base
  def initialize(message:)
    @message = message
  end
end
```

`# my_component.html.erb`

```erb
<h1><%= @message %><h1>
```

^ Take this example

^ two files side by side

^ (talk through code)

^ Follow a similar compilation process

---

`# my_component.rb`

```ruby
class MessageComponent < ActionView::Component::Base
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

# Unit testing

```ruby
RSpec.describe BoxComponent do
  it "renders message" do
    result = render_inline(MessageComponent, message: "Hello, World!")

    assert_includes result.text, "Hello, World!"
  end
end
```

^ Unit testing components is simple

^ Render component inline 

^ assert against rendered result

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

^ Some cool contributions include:

---

# `rails g component Example`

^ Simple things like 

^ Adding generator support

^ Vinicius Stock from Shopify

---

#[fit] `ActionView::Component::Preview`

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
  class BadgeComponentPreview < ActionView::Component::Preview
    def open
      render(Issues::BadgeComponent, state: :open)
    end

    def closed
      render(Issues::BadgeComponent, state: :closed)
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

# Beyond

^ for a while just focused on react ideas in rails

^ now thinking beyond

^ what can we do better than react

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

[.code-highlight: 7-11]

```html
<div class="Box">
  <div class="Box-header"><h3 class="Box-title">Box title</h3></div>
  <div class="Box-body">Box body</div>
  <div class="Box-footer">Box footer</div>
</div>

<Box>
  <BoxHeader>Box title</BoxHeader>
  <BoxBody>Box body</BoxBody>
  <BoxFooter>Box footer</BoxFooter>
</Box>
```

^ Here's what it might look like as a React component

^ S there are downsides

^ order of elements matters

^ enforce header is first?

^ enforce footer is last?

^ enforce title and body are required?

^ limited options as react only supports passing single block of content

---

```html
<Box>
  <BoxHeader>Box title</BoxHeader>
  <BoxBody>Box body</BoxBody>
  <BoxFooter>Box footer</BoxFooter>
</Box>

<Box header="Box title" footer="Box footer">
  Box body
</Box>
```

^ One solution would be to have Box take header and footer arguments

^ limits what we can pass for those arguments

^ couldn't pass another component for footer

---

```erb
<div class="Box">
  <div class="Box-header"><h3 class="Box-title">Box title</h3></div>
  <div class="Box-body">Box body</div>
  <div class="Box-footer">Box footer</div>
</div>
```

^ Go back to example HTML

^ rewrite as ActionView::Component

---

`# box_component.rb`

```ruby
class BoxComponent < ActionView::Component::Base
  def initialize
  end
end
```

`# box_component.html.erb`

```erb
<div class="Box">
  <div class="Box-header"><h3 class="Box-title">Box title</h3></div>
  <div class="Box-body">Box body</div>
  <div class="Box-footer">Box footer</div>
</div>
```

`# index.html.erb`

```erb
<%= render(BoxComponent) %>
```

^ start with a component that renders our example code

---

`# box_component.rb`

```ruby
class BoxComponent < ActionView::Component::Base
  def initialize
  end
end
```

`# box_component.html.erb`

```erb
<div class="Box">
  <%= content %>
</div>
```

`# index.html.erb`

```erb
<%= render(BoxComponent) do %>
  <%= render(BoxHeaderComponent) do %>Box title<% end %>
  <%= render(BoxBodyComponent) do %>Box body<% end %>
  <%= render(BoxFooterComponent) do %>Box footer<% end %>
<% end %>
```

^ Make it more like the react example

^ But really no better

^ but we're writing ruby, so we can do better

^ unlike javascript, ruby methods can accept multiple blocks

---

`# box_component.rb`

```ruby
class BoxComponent < ActionView::Component::Base
  def initialize
  end
end
```

^ back in component

---

[.code-highlight: 2]

`# box_component.rb`

```ruby
class BoxComponent < ActionView::Component::Base
  with_content_areas :header, :body, :footer

  def initialize
  end
end
```

^ we can declare multiple content areas

---

`# index.html.erb`

```erb
<%= render(BoxComponent) do %>
  <%= render(BoxHeaderComponent) do %>
    Box title
  <% end %>
  <%= render(BoxBodyComponent) do %>
    Box body
  <% end %>
  <%= render(BoxFooterComponent) do %>
    Box footer
  <% end %>
<% end %>
```

^ In template that renders component

^ refactor it

---

`# index.html.erb`

```erb
<%= render(BoxComponent) do |component| %>
  <% component.with(:header) do %>
    Box title
  <% end %>
  <% component.with(:body) do %>
    Box body
  <% end %>
  <% component.with(:footer) do %>
    Box footer
  <% end %>
<% end %>
```

^ to use named blocks instead of separate components

---

[.code-highlight: 1-3]
[.code-highlight: 6]
[.code-highlight: 6-7]
[.code-highlight: 6-8] 
[.code-highlight: 5-9] 

`# box_component.html.erb`

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

---

`# box_component.rb`

```ruby
class BoxComponent < ActionView::Component::Base
  with_content_areas :header, :body, :footer

  def initialize
  end
end
```

^ back in component

---

[.code-highlight: 4]

`# box_component.rb`

```ruby
class BoxComponent < ActionView::Component::Base
  with_content_areas :header, :body, :footer

  validates :header, :body, presence: true

  def initialize
  end
end
```

^ we can add a validation to require certain content areas to be set

---

# Ruby > Javascript

^ made me wonder

^ what other things can we do better than javascript?

^ PAUSE

---

# Performance

^ what about performance?

---

# 10's of k requests/sec

^ We serve a lot of requests

^ It's been a non-issue

^ Also easier to make fast

---

# templates * locals

^ remember how

^ method for each unique locals passed to template at runtime

---

# Caching

^ leads to less than optimal caching behavior

^ Cached at runtime, after forking servers like Unicorn and Puma

^ One part of cold first request render times being slow

^ Rails 6 contained some optimizations by John Hawthorn

^ Internal code in our app with a more extreme optimization

---

[.build-lists: true]

* Scan all templates for render calls
* Group by template
* Find unique combinations of locals
* Compile template for each combination

^ Scan 

^ S Group

^ S Uniq combinations of locals

^ S Compile for each

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

^ John Hawthorn is working on Rails improvements in this area

---

```ruby
class MessageComponent < ActionView::Component::Base
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

^ Easy way is to migrate a presenter / view model

^ what we've been doing

^ Linter to cap view model usage, directing to components instead

---

# Tests

^ Immediate testing benefit

^ Migrate unit tests from previous abstraction

^ Also migrate most controller tests

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

^ PAUSE

---

# The Future

^ what about the future

---

# Rails

^ goal to eventually incorporate into rails

---

![inline](img/rails-pr.png)

^ Started to make progress

^ Preliminary PRs in Rails for syntax

^ Continue to integrate more of library into Rails

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

---

# Change

^ world will keep changing

---

# It's up to us.

^ up to us to make thoughtful extractions

^ keep Rails relevant

---

# Time 

^ Our time is precious

^ How will you spend yours?

---

# Thanks.

^ What was confusing? What could I improve?

---