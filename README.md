This is a project that is designed to ask the user to input a number 
the function creaqted will chek whether the number belongs in the fibonacci sequence or not
the project is to be done in the python programming language with each step laid out carefully in this document

PREREQUISITE KNOWLDEGE:

The fibonnaci sequence is a sequence of numbers where each number after the second
number (or third number if counting from 0) is the sum of the two numbers that preceeded it.

FORMULAE:
 There are a few ways of finding out if a number is part of the fibonacci series or not

 a.
  binets fromula :
 for an integer n where Fn is the nth number in the sequence/series, Fn = (phi^n(1 - phi)^n )/ sqrt(5)
 where phi is a constant called the golden ratio = (1 + sqrt(5))/2 0r 1.6180
 it states that if Fn is a constant, then n is a part of the fibonacci series.


 b. 
  PREFECT SQUARES:  (prefered method)
  if a number n is part of a fibonacci series, then 5(n)^2 + 4 or 5(n)^2 - 4 is always a perfect square:
  this implies that we
  i. create a function perfectSquare(x) that checks if a number x is a perfect square and only returns True if so
  ii. call the first function in a second function fibNo() that checks whether the condition that either 5n^2 +4 or 5n^2 -4 or both will be perfect suqares given the number n is true
  iii. define a third function isFib(n) that checks if the number entered by the user meets the condition of the function fibNo and returns f'{N} is a fibonacci number', if True and opposite if not.

  to run this project use the commandline/terminal 
  type: py pthon_mini_project and press the enter key.