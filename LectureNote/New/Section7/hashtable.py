class HashTable:
    def __init__(self,size) -> None:
        self.data = [None]*size
    
    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        return hash

    def set(self, key, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value])
        return self.data
    
    def get(self, key):
        address = self._hash(key)
        if not self.data[address]:
            return "NO VALUE"
        for i in range(len(self.data[address])):
            if self.data[address][i][0] == key:
                return self.data[address][i][1]
        return "NO VALUE"

    def keys(self):
        keysArray = []
        for i in range(len(self.data)):
            if self.data[i]:
                keysArray.append(self.data[i][0][0])
        return keysArray


myHashTable = HashTable(2)
myHashTable._hash('grapes')
myHashTable.set('grapes',10000)
myHashTable.set('apple',54)
print(myHashTable.get('grapes'))
print(myHashTable.keys())
    