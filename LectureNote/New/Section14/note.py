"""
Searching + Traversing 
BFS + DFS

Searching is big part of our life, more and more website 

## Linear Search: we search one by one by traversing every element, Best:O(1), Worst O(n)
## Binery Search: O(logn), Sorted array, Binery Search Tree, It only requires the traversal through the one branch, which means height, divide and conqur
## Depth First Search: Traversal,  Left to Right, level to level, it will use the extra memory to track the node
## Breadth First Search: Traversal, 

The reason why we don't store in array, trees, insert&delete will have a advantages 

## BFS vs DFS
BFS: not good for finding whether there is a path
++ PLUS ++ 
Shortest Path
Closer Nodes

-- MINUS -- 
More Memory

DFS: not good for finding shortest path
++ PLUS ++ 
Less Memory
Does Path Exist?

-- MINUS --
Can Get Slow

## Questions

//If you know a solution is not far from the root of the tree:BFS
//If the tree is very deep and solutions are rare: BFS
//If the tree is very wide: DFS
//If solutions are frequent but located deep in the tree: DFS
//Determining whether a path exists between two nodes: DFS
//Finding the shortest path: BFS

## Preorder, InOrder, PostOrder
#      9 
#   4     20
# 1    6  15   170

# InOrder - 1,4,6,9,15,20,170
# PreOrder - 9,4,1,6,20,15,170
# PostOrder - 1,6,4,15,170,20,9

#Dijkstar + Bellman-Ford Algorithms
Shortest Path with weighted edges 
Dijkstar: cannnot accomodate negative weiths Better time complexity
Bellman-Ford can accomodate negative weights O(n^2) interms of time coplexity it's not good.
"""