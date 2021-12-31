class Array:
    def __init__(self):
        self.length = 0
        self.data = {}
    
    def get(self, index):
        return self.data[index]
    
    def push(self, item):
        self.data[self.length] = item
        self.length +=1 
        return self.length

    def pop(self):
        lastItem = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -=1
        return lastItem
    
    def delete(self, index):
        item = self.data[index]
        self.shiftItems(index)
    
    def shiftItems(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1


# Define
newArray = Array()

# Lookup
#print(newArray.get(0))

# Push
newArray.push('hi')
newArray.push('hello')
newArray.push('third')
newArray.push('Forth')
print(newArray.data, newArray.length)

# Pop
newArray.pop()
print(newArray.data, newArray.length)

# Delete
newArray.delete(1)
print(newArray.data, newArray.length)