"""
Trees: 
Data Structure which has hierachical structure
Root, Parent, Child, Leaf, Sibling

Any Website --> developer tool --> Document Object Model is one of the examples of trees
Family Trees, Twitter, Abstract Syntax Tree(how the program is run)
The beauty of trees is it uses the node of Linked List
Linked List is technically a type of tree, with more pointers

There are bunch of trees, and there are certain trees which is efficienct for some use cases

## Binary Trees
Type of tree with a few rule, each node have either 0, 1, 2 nodes

Perfect Binary Tree: The parent node has exactly 2 child except for the leaf nodes, all the nodes above + 1 = leaf node
Full Binary Tree: The parent node has 

## O(logN)
Perfect Binary Tree
Level 0: 2^0 = 1
Level 1: 2^1 = 2
Level 2: 2^2 = 4
Level 3: 2^3 = 8
Level 4: 2^4 = 16

# of Nodes = 2^(height) - 1
log(Nodes) = height

The maximum steps that we need for Binery Search Trees is heights which can be expressed by O(logN)
The efficiency comes from the characteristics that we don't need to check every element
Google search engine uses the tree structure as a fundamental technologies


## Bineary Search Trees: Data Structure that preserve the relationship between the nodes, 
1. All child node of the right of the parent node is larger than the parent node
2. All child node of the left of the parent node is smaller than the parent node
3. The node can only have upto 2 nodes

Lookup O(logN)
insert O(logN)
delete O(logN)

## Balanced VS Unbalanced BST
If the trees turn into long linked list it essentially let us search every element and we cannot take advantages of the O(logN)
The worst case for trees structure is O(n)

## BST Pros and Cons
++ PLUS ++
Better than O(n)
Ordered
Flexible Size

-- MINUS -- 
NO O(1) Operations
"""