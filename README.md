ultron
======

*I see a suit of armor around Math.SE...*

Math Stack Exchange is under constant attack by low quality questioners.  The goal of Ultron is to form a preemptive strike against low quality posts by immediate recognition, reporting, downvote, closure, and deletions.  Another side effect is to generate a list of high-quality, yet old, questions to be handled by our Crusaders.

How will it work?
-----------------

Right now, Ultron is still in the early developmental stages.  The general tactic is to train a Bayesian network to recognize low quality posts based off of factors like length, LaTeX usage, user age and reputation, etc.  To collect data, I'm going to perform analysis of my own votes (up, down, close, and deletion), as well as attempting to skim the low-quality posts and closure queue history.

Eventually, I'd like to perform automated duplicate checking, but it's still fairly difficult to search for mathematics.

The primary interface for the program will be StackExchange chat, specifically the Math.SE chatroom (and low-quality post room).  Since it will be hanging out in chat anyway, I've decided to add some "helpful" features (e.g. Wolfram Alpha API calls).  For the backend, I'm going to create a web-based framework (that way, I don't have to keep watching the terminal for errors, etc).

What's its status?
------------------

Ultron is still in its early development phases.  I've built the basic chatbot skeleton and the websocket reader for processing questions as they come in.  The next steps are to build and train the Bayesian network, make the chat interface more robust, then build a better backend.

What do I need to make this work?
---------------------------------

I'm developing on Ubuntu 14.04 with this repo in a `virtualenv`.  The packages I've installed thus far are:
  - `websocket-client`
  - `xmltodict`
  - `numpy`
  - `scipy`
  - `sklearn`

To manage all chatroom interaction, I use the [ChatExchange3](https://github.com/ByteCommander/ChatExchange3) project, which is added as a submodule in this repo.
