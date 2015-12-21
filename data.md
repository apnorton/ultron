Database
========

The Ultron codebase stores a "training set" of questions in a sqlite database.
This file describes what I'm storing in the database and a description of the
features (columns) I consider when doing classification.

Discrete Features
-----------------

  - **Tags**
  - **Presence of MathJax**

Continuous Features
-------------------

  - **Time of Posting**
  - **Words in Post**
  - **Post Score**
  - **Owner Rep**
  - **Number of "Banned" Words**

Classifications
---------------

  - **Ok** - Doesn't deserve any negative action (numeric value 0)
  - **Close** - Deserves a closevote (numeric value 1)
  - **Downvote** - Deserves a downvote (numeric value 2)

Other Database columns
----------------------

  - **Full text of post (HTML)**
  - **Post Title**
