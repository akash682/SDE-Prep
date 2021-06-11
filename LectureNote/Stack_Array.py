class Node ():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Stack():
    def __init__(self) -> None:
        self.array = []
        self.length = 0

    def peek(self):
        print(self.array[-1])

    def push(self,value):
        self.array.append(value)
        self.length += 1
        print(self.array)

    def pop(self):
        self.array.pop()
        self.length -= 1
        print(self.array)

myStack = Stack()

#Push 2 ,56, 12
myStack.push(2)
myStack.push(56)
myStack.push(12)

#Pop 12
myStack.pop()

# Peek 56
myStack.peek()