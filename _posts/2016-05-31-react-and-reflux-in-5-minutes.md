---
layout: post
title: React and Reflux in 5 minutes
---

_Note: This post was originally published on the [MojoTech blog](https://www.mojotech.com/blog/). It's been reproduced here for posterity._

One of the fastest-changing areas in web development is front-end JavaScript frameworks. Once you've figured out which framework to use, there is the daunting task of identifying best practices. Here's why we picked React/Reflux, and how we made it work for us.

I was recently tasked with overhauling the process one of our clients uses to review user-created content for copyright violations. Among the requirements of the new application was a stipulation for a performant, asynchronous process that wasn't a good fit for the traditional request/response cycle. Up until then, we had avoided using a front-end JavaScript framework, as the associated overhead did not add any business value for the client. Now it would.

In considering our options, simplicity and ease of implementation were our top priorities. We decided that React would be a great fit for the application, since we could easily make reusable components that would be of value in other features, and Reflux gave us simple uni-directional data flow to manage the application state.

As we built the app, we were impressed with how simple the React/Reflux APIs were. However, it was hard to find good examples of best practices/patterns along the way, and wished there was a code-complete example of how to build a simple application that consumed a RESTful resource. We're here to fix that.

## Reflux Data Flow

The Reflux uni-directional data flow has three parts: Stores, React Components, and React Actions. Stores manage state, Components listen for updates from Stores, and Components trigger React Actions, to which Stores listen.

Here's how that Reflux flow worked in our app:

0. Store loads content blob to review from JSON endpoint
0. Component(s) listen for store update with content blob
0. Review component triggers updateStatus action, marking the review as approved/rejected in the store
0. Review component triggers submitReview action, telling the store to submit the review to the API and load the next review

![App flow](/img/posts/2016-05-31-react-and-reflux-in-5-minutes/react-hi-res.png)

## Actions

In `app/assets/javascripts/actions/content_reviewer_actions.js`:

```js
var Reflux = require('reflux');

var ContentReviewerActions = Reflux.createActions({
  // Child actions 'completed' and 'failed' are called by resolution of listenAndPromise
  "loadReview": { children: ['completed', 'failed'] },
  "updateStatus": {},
  "submitReview": {}
});

// Reflux actions can trigger server calls, which we use to load the content to review
ContentReviewerActions.loadReview.listenAndPromise( function() {
  return $.ajax({
    type: "GET",
    url: Routes.content_reviews_path({ format: 'json' })
  });
});

module.exports = ContentReviewerActions;
```

## Store

In `app/assets/javascripts/stores/content_reviewer_store.js`:

```js
var Reflux = require('reflux');
var ContentReviewerActions = require('../actions/content_reviewer_actions');

var ContentReviewerStore = Reflux.createStore({
  // Shorthand for listening to all ContentReviewerActions
  listenables: ContentReviewerActions,

  data: {},

  // Load a review when the store is initialized
  init: function() {
    ContentReviewerActions.loadReview();
  },

  // Clear out the current review and any errors while we load the next review
  onLoadReview: function() {
    this.data.review = null;
    this.data.loadError = null;

    this.trigger(this.data);
  },

  // Called from ContentReviewerActions.loadReview.listenAndPromise
  onLoadReviewCompleted: function(res) {
    this.data.review = res.review;
    this.data.loadError = res.error;

    this.trigger(this.data);
  },

  // Called from ContentReviewerActions.loadReview.listenAndPromise
  onLoadReviewFailed: function() {
    this.data.loadError = "Could not load review.";

    this.trigger(this.data);
  },

  // Update status, pass updated state back to component(s)
  onUpdateStatus: function(status) {
    this.data.review.status = status;

    this.trigger(this.data);
  },

  // Submit current review while we load the next one
  onSubmitReview: function() {
    this.submitReview();
    ContentReviewerActions.loadReview();
  },

  // When we need to reference store data in our server requests, it's easier
  // to handle the communication in the store instead of the actions.
  submitReview: function() {
    $.ajax({
      type: "PUT",
      url: Routes.review_path(this.data.review.review_id, { operation: this.data.review.status })
    }).done(function(res) {
      // Success notification
    }).fail(function(xhr) {
      // Error notification
    });
  }
});

module.exports = ContentReviewerStore;
```

## Component

In `app/assets/javascripts/components/content_reviewer.js`

```jsx
var React = require('react');
var Reflux = require('reflux');
var ContentReviewerStore = require('../../stores/content_reviewer_store');
var ContentReviewerActions = require('../../actions/content_reviewer_actions');

var ContentReviewer = React.createClass({
  // Connects this.state in component to this.data in store
  mixins: [ Reflux.connect(ContentReviewerStore, "review") ],

  render: function () {
  // Typically each of these branches would be its own component. I've inlined them here for simplicity's sake.
  if (this.state.review) {
    return (
      <div>
        <h1>{ this.state.review.review_id }</h1>
        <button onClick={ this._markApproved }>Approve</button>
        <button onClick={ this._markRejected }>Reject</button>
        <button onClick={ this._submitReview }>Submit</button>
      </div>
    )
  } else if (this.state.loadError) {
    return (
      <h1 className="alert">{ this.state.loadError }</h1>
    )
  } else {
    return (
      <span>"Loading"</span>
    )
  }
  },

  _markApproved: function() {
    ContentReviewerActions.updateStatus("approved");
  },

  _markRejected: function() {
    ContentReviewerActions.updateStatus("rejected");
  },

  _submitReview: function() {
    ContentReviewerActions.submitReview();
  }
});

module.exports = ContentReviewer;
```

Since deploying the initial project, we've gone on to build several more React/Reflux applications. Since we took the time to build reusable components with clearly defined interfaces, we've been able to use them in each new application. Instead of spending time writing duplicative code, we're able to focus on further improving our shared set of components, the benefits of which trickle down to each application.

In addition, the constraint of uni-directional data flow makes reasoning about the state of the application incredibly simple. This has been a huge productivity win for our team, as it makes it much easier to debug state-related problems.