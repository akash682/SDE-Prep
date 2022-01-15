from hashlib import new
from multiprocessing.sharedctypes import Value
from reprlib import aRepr
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
                            leftmostParet = leftmost
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
print("hello")