class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.pointer = None

class LinkedList():
    def __init__(self, value) -> None:
        self.head = Node(value)
        self.tail = self.head
        self.length = 1
    
    def append(self, value):
        newNode = Node(value)
        self.tail.pointer = newNode
        self.tail = newNode
        self.length += 1

    def prepend(self, value):
        newNode = Node(value)
        newNode.pointer = self.head
        self.head = newNode
        self.length += 1 
    
    def insert(self, index, value):
        newNode = Node(value)
        currentNode = self.head
        for i in range(index-1):
            currentNode = currentNode.pointer
        newNode.pointer = currentNode.pointer
        currentNode.pointer = newNode
        self.length +=1

    def remove(self, index):
        currentNode = self.head
        for i in range(index-1):
            currentNode = currentNode.pointer
        currentNode.pointer = currentNode.pointer.pointer
        self.length -= 1
    
    def reverse(self):
        if self.length == 1:
            return self.head
        first = self.head
        second = first.pointer
        while(second):
            tmp = second.pointer
            second.pointer = first
            first = second
            second = tmp
        self.head.pointer = None
        self.head = first
    
    def printLL(self):
        result = []
        currentNode = self.head
        while(currentNode != None):
            result.append(currentNode.value)
            currentNode = currentNode.pointer
        print(result)
        
            

myLinkedList = LinkedList(10)
myLinkedList.printLL()

myLinkedList.append(20)
myLinkedList.printLL()

myLinkedList.append(15)
myLinkedList.printLL()

myLinkedList.prepend(30)
myLinkedList.printLL()

myLinkedList.insert(2,30)
myLinkedList.printLL()

myLinkedList.remove(2)
myLinkedList.printLL()

myLinkedList.reverse()
myLinkedList.printLL()