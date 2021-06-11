"""
Binary Tree
Bineary tree is a tree in which the node can only have 0, 1, 2 nodes.
Perfect Binary Tree: Each node has exactly 2 childs. This is efficient. 1 --> 2 --> 4 --> 8. 
Number of nodes on the bottom level = Number of all the left over node + 1
About half of the node are on the bottom.

Binary Search Tree
lookup O(logN)
insert O(logN)
delete O(logN)

Level 0: 2^0 = 1
Level 1: 2^1 = 2
Level 2: 2^2 = 4
Level 3: 2^3 = 8
...
Level n: 2^n

# of Nodes = 2^h - 1
log nodes = height


Binary Search Trees
WHy? not hash table? 
Because it persists the relationships between the element so called as node.
This characteristics can be applied to the structure for like folder where we have a root folder and subfolder so that and so on.

Rule
1. If you go to the right, the value increases.
2. IF you go to the left, the value decreases.
3. Node can only have upto 2 nodes.

Problem
Balanced vs Unvalanced 
If it goes long linked list and have to loop through all the node which result in O(n)
Average O(logn) Worst O(n)
We need to be able to talk about balancing the binary search trees.

BST 
Pros: Better than O(n), Ordered(Compare with Hash table relationship and hierarchical structure), Flexible Size
Cons: No O(1) operations. We need to have some sort of traversal!
"""

class BinaryTree():
    def __init__(self, value) -> None:
        self.val = value
        self.left = None
        self.right = None