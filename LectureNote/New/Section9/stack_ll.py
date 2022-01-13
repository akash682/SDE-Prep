class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack():
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0
    
    def peek(self):
        return self.top.value
    
    def push(self, value):
        newPlate = Node(value)
        newPlate.next = self.top
        self.top = newPlate
        if not self.bottom:
            self.bottom = newPlate
        self.length += 1
           
    def pop(self):
        popNode = self.top
        self.top = self.top.next
        self.length -= 1
        return popNode

myStack = Stack()
myStack.push(3)
myStack.push(4)
myStack.push(5)
print(myStack.peek())
print(myStack.pop())
print(myStack.peek())
