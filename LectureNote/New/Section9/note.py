"""
Stacks + Queues
Linear Data Structures

The only difference is how the data is removed

## Stacks: LIFO Last in First Out, Stack on top of each other, i.e. stack of plate
Lookup: O(n)
Pop O(1)
Push O(1)
Peek O(1)

Example: Programming language is built with stacks, last in first out; 
def a
    def b
        pass
a in --> b in --> b out --> a out

Example: Web Browser

## Queues: First in First Out, The first person arrives in line gets to go first, i.e. entrace line
Lookup: O(n)
Enqueue: O(1)
Dequeue: O(1)
Peek: O(1)

Uber, Reservation, Printer, 
Creating a array using queue is really bad because we need to shift every element

## Stacks Vs Queues
# Stacks
twitter 
youtube
udemy.com
can be created using arrays and linked lists
Arrays: 
Linked Lists: 

# Queues
Matt -- Joy -- Samir -- Pavel
can be created using arrays and linked lists

if we use array to build a queue, dequeue will be a nightmare 
because it requires O(n) operation 
If we use LinkedList to build a queue , it requries O(1) operation 


## Stacks vs Queues
++ PLUS ++
Fast Operations
Fast Peek
Ordered

-- MINUS --
Slow Lookup

Really useful while it's used in a restricted way
"""