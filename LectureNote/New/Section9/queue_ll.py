class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Queue():
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0
    
    def peek(self):
        return self.first.value
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.last = newNode
            self.first = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1
                
    def dequeue(self):
        if self.first == None:
            return None
        else:
            popNode = self.first
            self.first = self.first.next
            self.length -= 1
            return popNode.value
            

myQueue = Queue()
myQueue.enqueue(3)
myQueue.enqueue(4)
myQueue.enqueue(5)
print(myQueue.peek())
print(myQueue.dequeue())
print(myQueue.peek())