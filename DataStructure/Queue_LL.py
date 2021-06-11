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
        val = self.first.value
        print(val)
    
    def enqueue(self,value):
        newNode = Node(value)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            lastNode = self.last
            lastNode.next = newNode
            self.last = newNode
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        if self.first == self.last:
            self.last = None
        currentNode = self.first
        self.first = currentNode.next
        self.length -= 1

    def printll(self):
        array = []
        currentNode = self.first
        while(currentNode != None):
            array.append(currentNode.value)
            currentNode = currentNode.next
        print(array)

# Initialize the Queue
myQueue = Queue()

# Enqueue 2
myQueue.enqueue(2)
myQueue.printll()

# Enqueue 5
myQueue.enqueue(5)
myQueue.printll()

# Enqueue 12
myQueue.enqueue(12)
myQueue.printll()

# Dequeue 2
myQueue.dequeue()
myQueue.printll()

# Enqueue 12
myQueue.enqueue(12)
myQueue.printll()

myQueue.peek()