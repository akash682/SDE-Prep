from typing import NewType


class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.pointer = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self, value) -> None:
        self.head = Node(value)
        self.tail = self.head
        self.length = 1
    
    def append(self, value):
        newNode = Node(value)
        newNode.prev = self.tail
        self.tail.pointer = newNode
        self.tail = newNode
        self.length += 1

    def prepend(self, value):
        newNode = Node(value)
        self.head.prev = newNode
        newNode.pointer = self.head
        self.head = newNode
        self.length += 1 
    
    def insert(self, index, value):
        newNode = Node(value)
        currentNode = self.head
        for i in range(index-1):
            currentNode = currentNode.pointer
        currentNode.pointer.prev = newNode
        newNode.prev = currentNode
        newNode.pointer = currentNode.pointer
        currentNode.pointer = newNode
        self.length +=1

    def remove(self, index):
        currentNode = self.head
        for i in range(index-1):
            currentNode = currentNode.pointer
        currentNode.pointer.prev = currentNode
        currentNode.pointer = currentNode.pointer.pointer
        self.length -= 1
    
    def printLL(self):
        result = []
        currentNode = self.head
        while(currentNode != None):
            result.append(currentNode.value)
            currentNode = currentNode.pointer
        print(result)
        
            

myDoublyLinkedList = DoublyLinkedList(10)
myDoublyLinkedList.printLL()

myDoublyLinkedList.append(20)
myDoublyLinkedList.printLL()

myDoublyLinkedList.append(15)
myDoublyLinkedList.printLL()

myDoublyLinkedList.prepend(30)
myDoublyLinkedList.printLL()

myDoublyLinkedList.insert(2,30)
myDoublyLinkedList.printLL()

myDoublyLinkedList.remove(2)
myDoublyLinkedList.printLL()