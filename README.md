CS4100 Project
==============

This is the repository for code used by Mathias Kools and Jamie Kuesel for their final CS 4100 project.
Our original goal was to explore solving 3-dimensional variants of simple 2d games we knew.

## Style and Navigating

Mathias tries to run pylint (version 2.6) without any configuration on all of the source code,
and fix the errors that he sees.
This is mentioned because it means every module / file should have a docstring explaining what it does.

## Requirements

To run this source code, Mathias used Python 3.6.
The following 3rd-party libraries were used.
 - numpy (version 1.19.5)
   This library was selected for the easy to use matrices.
   The slicing syntax was invaluable for generalizing game-won checks.
 - blessed (version 1.18)
   This library was selected as a simple library to construct a terminal interface for playing tic tac toe.