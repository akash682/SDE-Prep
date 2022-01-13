class Stack():
    def __init__(self) -> None:
        self.stack = []
    
    def peek(self):
        if not self.stack:
            return None
        else:
            return self.stack[-1]
    
    def push(self, value):
        self.length += 1
        self.stack.append(value)
           
    def pop(self):
        self.length -= 1
        return self.stack.pop()

myStack = Stack()
myStack.push(3)
myStack.push(4)
myStack.push(5)
print(myStack.peek())
print(myStack.pop())
print(myStack.peek())