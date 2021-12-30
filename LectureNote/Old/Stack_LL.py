class Node ():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Stack():
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        tmp = self.top
        print(self.top.value)

    def push(self,value):
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode
        if self.length == 0:
            self.bottom = newNode
        self.length += 1
        self.printll()

    def pop(self):
        currentNode = self.top
        if (not currentNode):
            return None
        if (self.top == self.bottom):
            self.bottom = None
        self.top = currentNode.next
        self.length -= 1
        self.printll()

    def printll(self):
        array = []
        currentNode = self.top
        while(currentNode != None):
            array.append(currentNode.value)
            currentNode = currentNode.next
        print(array)

myStack = Stack()

#Push 2 ,56, 12
myStack.push(2)
myStack.push(56)
myStack.push(12)

#Pop 12
myStack.pop()

# Peek 56
myStack.peek()