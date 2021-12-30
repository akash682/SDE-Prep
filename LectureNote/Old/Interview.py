"""
Interview 

How to solve the problem?

* Will you solve the companies problem?
--> Thought Process, You dont memorize but understand the tradeoffs
--> BigO, How to solve problems
--> Data Structures Algorithms

1. Analytic Skills
2. Coding Skills
3. Technical Skills
4. Communication Skills

What we need to know for Coding Interviews?
Data Structures
* Array
* Stacks
* Queues
* Linked Lists
* Trees
* Tries
* Graphs
* Hash Tables

Algorithms
* Sorting
* Dynamic Programming
* BFS + DFS (Serching)
* Recursion

Readablity
Time Complexity
Space Conplexity
"""

"""
Given 2 arrays, create a function that let's a user know True/False whether these two arrays contain any common items
For example:

const array1 = ['a','b,'c','d']
const array2 = ['x','y','z']
False

const array1 = ['a', 'b', 'c', 'x']:
const array2 = ['z', 'y', 'x']
True

should return true
https://github.com/peterlamar/python-cp-cheatsheet
https://github.com/gto76/python-cheatsheet
"""


cars = ['Ford', 'B', 'Volvo']
cars.sort(key=lambda x: len(x) )
print(cars)