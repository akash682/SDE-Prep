"""
Trees are data structure that has hierarchical structure

Root Node Child Node Leaf Node, Siblings
It's like a inverse tree

Abstract Syntax Tree
Linked list is a type of tree and it's linear and only one way
Node can only point to the child
Node don't really have to point the root

Binary Tree
Bineary tree is a tree in which the node can only have 0, 1, 2 nodes.
Perfect Binary Tree: Each node has exactly 2 childs. This is efficient. 1 --> 2 --> 4 --> 8. 
Number of nodes on the bottom level = Number of all the left over node + 1
About half of the node are on the bottom.

Binary Search Tree
lookup O(logN)
insert O(logN)
delete O(logN)
"""

class BinaryTree():
    def __init__(self, value) -> None:
        self.val = value
        self.left = None
        self.right = None