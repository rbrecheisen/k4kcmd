# k4kcmd

This is a command-line interpreter that kids can use to learn programming in Python. The 
idea is to first teach them the basics of Python and then let them build a simple game
using the Pygame package.

# architecture and design

The course consists of a number of lessons. It might be a good idea to use the same setup
as R's swirl package. Check out the docs for that. 

## swirl

Swirl is built around the concept of courses that contain one or more lessons. Each lesson
consists of one or more questions. There are different types of questions, e.g., so-called 
meta questions that just contain some information about the course. There are message 
questions that also just present some information to the user, like a bit of theory before
you move on to practice. Then there are command questions which require the user to type in
a command or expression. Command questions require exact input, i.e., the user should type
in exactly what is expected. Multiple choice questions are exactly that. They offer the user
multiple choices to choose from. Figure questions are similar to message questions except
they show the user graphical output. Video/URL questions allow the user to open a URL to 
somewhere, e.g., a video. Numerical questions require the user to type in a number. Text
questions require textual answers. Script questions ask the user to write a piece of script
that produces a certain output that is checked.

## k4kcmd anwser/testing

In K4Kcmd questions are just a piece of text together with an input field where the user can
type in some answer. Instead of literally checking the user's input and comparing it verbatim
to the true answer, we define a function that tries to interpret what the user typed in and 
determine the answer from that. How would that work for the different types of questions?

(1) Message questions. These are just pieces of text that are presented for informative
reasons. The user only has to click a button to continue.

(2) Script questions. These are pieces of code that the user must type in. We expect a certain
output from this code, so we actually try to run this code in Python and see what comes out.
Whatever comes out is compared to the true output. The results are displayed to the user. A
problem occurs when the user mistypes code, i.e., makes a typo making the code throw an exception.
What do we do then? Each user input should be caught by a try-catch that presents a Dutch language
error message that the user can work with.

