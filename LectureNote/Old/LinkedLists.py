
"""
Linked List 
Single/Double 

Head ------> Tail
Array
Bad time complexity --> insert, delete O(n)

Hash
O(1) but not ordered!

Singly linked list 
Value/Pointer 
Head(First Node) -------------------------> Tail(Last Node)
Current Memory Location/Next Memory Location 

linked list: apples --> grapes --> pears 

apples 
8947 ---> grapes
           8632 -----> orange
                       5783
https://visualgo.net/en/list

Traversal --> Slower than Arrays because it's disperse and scattered all over memory(in array it's close together)

prepend --> O(1)
append --> O(1)
lookup --> O(n)
insert --> O(n)
delete --> O(n)

What i pointer?
Pointer is a memory address location that stores the data.


"""
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, value) -> None:
        self.head = Node(value)
        self.tail = self.head
        self.length = 1
        
    
    def append(self, value):
        newNode = Node(value)
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1

    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def printList(self):
        array = []
        currentNode = self.head
        while(currentNode != None):
            array.append(currentNode.value)
            currentNode = currentNode.next
        print(array)

    def insert(self, index, value):
        currentNode = self.head
        for i in range(index-1):
            currentNode = currentNode.next

        newNode = Node(value)
        newNode.next = currentNode.next
        currentNode.next = newNode
        self.length += 1

    def delete(self, index):
        currentNode = self.head
        for i in range(index-1):
            currentNode = currentNode.next
        currentNode.next = currentNode.next.next
        self.length -= 1   

    def reverse(self):
        first = self.head
        self.tail = self.head
        second = first.next
        while second:
            tmp = second.next
            second.next = first
            first = second
            second = tmp
        
        self.head.next = None
        self.head = first
            
        

linkedlist = LinkedList(10)
linkedlist.append(15)
linkedlist.append(-5)
linkedlist.prepend(45)
linkedlist.insert(2,5)
linkedlist.delete(2)
linkedlist.printList()
linkedlist.reverse()
linkedlist.printList()


