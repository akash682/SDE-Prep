class Node():
    def __init__(self, value, node) -> None:
        self.value = value
        self.pointer = node

class LinkedList():
    def __init__(self, value) -> None:
        self.head = Node(value, None)
        self.tail = self.head
        self.length = 1
    
    def append(self, value):
        node = Node(value, None)
        self.head.pointer = node
        self.tail = node
        self.length += 1

myLinkedList = LinkedList(10)
print(myLinkedList)

myLinkedList.append(20)
print(myLinkedList)
