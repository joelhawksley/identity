---
layout: post
title: Encapsulating Ruby on Rails views
---

_Note: This post was originally published on the [GitHub blog](https://github.blog/). It's been reproduced here for posterity._

With the recent release of version 6.1, Ruby on Rails now supports the [rendering of objects](https://guides.rubyonrails.org/layouts_and_rendering.html#rendering-objects) that respond to `render_in`, a change [we](https://github.com/rails/rails/pull/36388) [introduced](https://github.com/rails/rails/pull/37919) to the framework. It may be small (the two pull requests were less than a dozen lines), but this change has enabled us to develop a framework for building encapsulated views called [ViewComponent](https://github.com/github/view_component).

## Why encapsulation matters

Unlike models and controllers, Rails views are not encapsulated. All Rails views in an application exist in a single execution context, meaning they can share state. This makes them hard to reason about and difficult to test, as they cannot be easily isolated.

The need for a new way of building views in our application emerged as the number of templates in the GitHub application grew into the thousands. We depended on a combination of presenters and partials with inline Ruby, tested by expensive integration tests that exercise the routing and controller layers in addition to the view layer.

Inspired by our experience building component-based UI with React, we set off to build a framework to bring these ideas to server-rendered Rails views.

## Enter ViewComponent

We created the ViewComponent framework for building reusable, testable & encapsulated view components in Ruby on Rails. A ViewComponent is the combination of a Ruby file and a template file. For example:

_test_component.rb_

```ruby
class TestComponent < ViewComponent::Base
  def initialize(title:)
    @title = title
  end
end
```

_test_component.html.erb_

```erb
<span title="<%= @title %>">
  <%= content %>
</span>
```

Which is rendered in a view:

```erb
<%= render(TestComponent.new(title: "my title")) do %>
  Hello, World!
<% end %>
```

Returning:

```html
<span title="my title">Hello, World!</span>
```

Unlike traditional Rails views, ViewComponent templates are executed within the context of the ViewComponent object, encapsulating their state and allowing them to be unit tested in isolation.

For example, to test our TestComponent, we can write:

```ruby
require "view_component/test_case"

class MyComponentTest < ViewComponent::TestCase
  def test_render_component
    render_inline(TestComponent.new(title: "my title")) { "Hello, World!" }

    assert_selector("span[title='my title']", text: "Hello, World!")
    # or, to just assert against the text:
    assert_text("Hello, World!")
  end
end
```

These kinds of unit tests enable us to test our view code directly, instead of via controller tests. They are also significantly faster: in the GitHub codebase, component unit tests take around 25 milliseconds each, compared to about six seconds for controller tests.

## In practice

Over the past two years, we’ve made significant strides in using ViewComponent: we now have over 400 components used in over 1600 of our 4500+ templates. For example, every [Counter](https://primer.style/view-components/components/counter) and [Blankslate](https://primer.style/view-components/components/blankslate) on GitHub.com is rendered with a ViewComponent.

We’re seeing several significant benefits from this architecture. Because ViewComponents can be unit tested against their rendered DOM, we’ve been able to reduce duplication of test coverage for shared templates, which we previously covered with controller tests. And since ViewComponent tests are so fast, we’re finding ourselves writing more of them, leading to higher confidence in our view code.

We’ve also seen the positive impact of the consistency that component-driven view architecture can provide. When we implemented a ViewComponent for the status of pull requests, we discovered several locations where we had not updated our previous, copy-pasted implementation, to handle the then-recently-shipped draft pull request status. By standardizing on a source of truth for the UI pattern, we now have a single, consistent implementation.

To see some of the ViewComponents we’re using in the GitHub application, check out the [Primer ViewComponents](https://primer.style/view-components/) library.

_Support for 3rd-party component frameworks such as ViewComponent is just one of many contributions GitHub engineers contributed to Rails 6.1. Other notable additions include [support for horizontal sharding](https://github.com/rails/rails/pull/38531), [strict loading](https://github.com/rails/rails/pull/37400), and [template annotations](https://github.com/rails/rails/pull/38848)._