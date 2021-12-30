"""
Doubly Linked List
prepend O(1)
append O(1)
lookup O(n)
insert O(n)
delete O(n)

It's exactly similar to singly linked list but contains this additional pointer to the previous node
It can traverse backwards.
Negative --> The characteristic that it holds the additional pointer may consume some memory
"""

from typing import final


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.before = None

class DubLinkedList():
    def __init__(self, value) -> None:
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self,value):
        newNode = Node(value)
        newNode.before = self.tail
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1

    def prepend(self,value):
        newNode = Node(value)
        newNode.next = self.head
        self.head.before = newNode
        self.head = newNode
        self.length += 1

    def insert(self,index,value):
        currentNode = self.head
        for i in range(index-1):
            currentNode = currentNode.next
        
        newNode = Node(value)
        newNode.before = currentNode
        newNode.next = currentNode.next

        currentNode.next.before = newNode
        currentNode.next = newNode
        self.length += 1
    
    def delete(self,index):
        currentNode = self.head
        for i in range(index-1):
            currentNode = currentNode.next
        
        currentNode.next = currentNode.next.next
        currentNode.next.before = currentNode
        self.length -= 1

    def printList(self):
        array = []
        currentNode = self.head
        while(currentNode != None):
            array.append(currentNode.value)
            currentNode = currentNode.next
        print(array)


linkedlist = DubLinkedList(10)
linkedlist.append(15)
linkedlist.printList()

linkedlist.append(-5)
linkedlist.printList()

linkedlist.prepend(45)
linkedlist.printList()

linkedlist.insert(2,5)
linkedlist.printList()

linkedlist.delete(2)
linkedlist.printList()


