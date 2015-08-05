ultron
======

*I see a suit of armor around Math.SE...*

Math Stack Exchange is under constant attack by low quality questioners.  The goal of Ultron is to form a preemptive strike against low quality posts by immediate recognition, reporting, downvote, closure, and deletions.  Another side effect is to generate a list of high-quality, yet old, questions to be handled by our Crusaders. 

How will it work?
-----------------

Right now, Ultron is still in the planning stages.  The general tactic is to train a Bayesian network to recognize low quality posts based off of factors like length, LaTeX usage, user age and reputation, etc.  To collect data, I'm going to perform analysis of my own votes (up, down, close, and deletion), as well as attempting to skim the low-quality posts and closure queue history.

Eventually, I'd like to perform automated duplicate checking, but it's still fairly difficult to search for mathematics.

What's its status?
------------------

Ultron is still in the conceptual phases.  This will be a fairly large project, so proper design is a must.

What do I need to make this work?
---------------------------------

I'm developing on Ubuntu 14.04 with this repo in a `virtualenv`.  The packages I've installed thus far are:
  - `websocket-client`
