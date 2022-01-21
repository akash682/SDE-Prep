from hashlib import new
from multiprocessing.dummy import current_process
from multiprocessing.sharedctypes import Value
import queue
from reprlib import aRepr, recursive_repr
from sre_constants import CATEGORY_UNI_LINEBREAK
from turtle import left


class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, value):
        newNode = Node(value)
        if not self.root:
            self.root = newNode
        else:
            curNode = self.root
            while True:
                if curNode.value < newNode.value:
                    if curNode.right == None:
                        curNode.right = newNode
                        break
                    else:
                        curNode = curNode.right
                else:
                    if curNode.left == None:
                        curNode.left = newNode
                        break
                    else:
                        curNode = curNode.left

    def lookup(self, value):
        if not self.root:
            return False
        else:
            curNode = self.root
            while True:
                if curNode.value < value:
                    if curNode.right == None:
                        return False
                    else:
                        curNode = curNode.right
                elif curNode.value > value:
                    if curNode.left == None:
                        return False
                    else:
                        curNode = curNode.left
                else:
                    if curNode.value == value:
                        return True
    
    def remove(self, value):
        if not self.root:
            return False
        else:
            currentNode = self.root
            parentNode = None
            while currentNode:
                if currentNode.value > value:
                    parentNode = currentNode
                    currentNode = currentNode.left
                elif currentNode.value < value:
                    parentNode = currentNode
                    currentNode = currentNode.right
                elif currentNode.value == value:
                    # Right Child is None
                    if currentNode.right == None:
                        if parentNode == None:
                            self.root = currentNode.left
                        else:
                            if currentNode.value < parentNode.value:
                                parentNode.left = currentNode.left
                            elif currentNode.value > parentNode.value:
                                parentNode.right = currentNode.left
                    # Right Child doesn't not have left child.
                    elif currentNode.right.left == None:
                        if parentNode == None:
                            self.root = currentNode.left
                        else:
                            currentNode.right.left = currentNode.left
                            if currentNode.value < parentNode.value:
                                parentNode.left = currentNode.right
                            elif currentNode.value > parentNode.value:
                                parentNode.right = currentNode.right
                    # Right Child have left child
                    else:
                        leftmost = currentNode.right.left
                        leftmostParent = currentNode.right
                        while leftmost.left != None:
                            leftmostParent = leftmost
                            leftmost = leftmost.left
                        
                        leftmostParent.left = leftmost.right
                        leftmost.left = currentNode.left
                        leftmost.right = currentNode.right

                        if parentNode == None:
                            self.root = leftmost
                        else:
                            if currentNode.value < parentNode.value:
                                parentNode.left = leftmost
                            elif currentNode.value > parentNode.value:
                                parentNode.right = leftmost
                return True
                        
    def breadthfirstSearch(self):
        currentNode = self.root
        list = []
        queue = []
        queue.append(currentNode)

        while len(queue) > 0:
            currentNode = queue.pop(0)
            list.append(currentNode.value)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        
        return list
    
    def breadthfirstSearchR(self, queue, list):
        if not len(queue):
            return list
        currentNode = queue.pop(0)
        list.append(currentNode.value)
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
        return self.breadthfirstSearchR(queue, list)
    
    def DFSInorder(self):
        return self.traverseInOrder(self.root, [])
    
    def DFSPreorder(self):
        return self.traversePreOrder(self.root, [])

    def DFSPostOrder(self):
        return self.traversePostOrder(self.root, [])

    def traverseInOrder(self, node, list):
        if node.left:
            self.traverseInOrder(node.left, list)
        list.append(node.value)
        if node.right:
            self.traverseInOrder(node.right, list)
        return list
    
    def traversePreOrder(self, node, list):
        list.append(node.value)
        if node.left:
            self.traversePreOrder(node.left, list)
        if node.right:
            self.traversePreOrder(node.right, list)
        return list

    def traversePostOrder(self, node, list):
        if node.left:
            self.traversePostOrder(node.left, list)
        if node.right:
            self.traversePostOrder(node.right, list)
        list.append(node.value)
        return list
        
        


myTree = BinarySearchTree()
myTree.insert(9)
myTree.insert(4)
myTree.insert(6)
myTree.insert(20)
myTree.insert(170)
myTree.insert(15)
myTree.insert(1)


print(myTree.lookup(15))
print(myTree.lookup(21))
print(myTree.breadthfirstSearch())
print(myTree.breadthfirstSearchR([myTree.root], []))
print(myTree.DFSInorder())
print(myTree.DFSPreorder())
print(myTree.DFSPostOrder())

