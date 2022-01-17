"""
Algorithm can make the time complexity to much more faster than O(n)

## Recursion
Recursive function is a function that calls itself.
Stack Overflow: Programming language deals with the nested function with the stack LIFO. 
which means we might encounter some cases that the call the function in the function itself we might use up the memory space 

## Recursion
# Identigy the base case
# Identify the recursive case
# Get closer and closer and return when needed. Ususally you have 2 returns

## Recursive vs Iterative
Anything you do with a recursion Can be done iteratively(loop)
Some problem can be described in easy coding 
It makes the code dry, do not repeat the code itself
less loops happening, it's not always a good decision

++ PLUS ++
DRY
Readablility

-- MINUS --
Large Stack

Trees: BFS + DFS (Recursion is preffered)
Everytime you are using a tree or converting something into a tree, consider recursion
1. Divided into a number of subproblems that are smaller instances of the same problem.
2. Each instance of the subproblem is identical in nature
3. The solutions of each subproblem can be combined to solve the problem at hand.

Divide and Concur using Recursion

"""
print("hello")

def inception(counter):
    if counter > 3:
        return 'done'
    counter += 1
    return inception(counter)

counter = 0
print(inception(counter))