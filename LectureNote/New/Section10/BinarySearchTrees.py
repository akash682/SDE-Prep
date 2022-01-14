from hashlib import new
from multiprocessing.sharedctypes import Value


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
            curNode = self.root
            prevNode = None
            lmoneNode = None
            while True:
                if curNode.value < value:
                    if curNode.right == None:
                        return False
                    else:
                        prevNode = curNode
                        curNode = curNode.right
                elif curNode.value > value:
                    if curNode.left == None:
                        return False
                    else:
                        prevNode = curNode
                        curNode = curNode.left
                else:
                    if curNode.value == value:
                        curNode = curNode.right
                        while curNode.left:
                            lmoneNode = curNode
                            curNode = curNode.left
                        


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