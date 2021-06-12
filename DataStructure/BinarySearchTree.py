class Node():
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value
    

class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, value):
        
        newNode = Node(value)
        
        if self.root == None:
            self.root = newNode
        else: 
            currentNode = self.root
            while True:
                if newNode.value < currentNode.value:
                    if currentNode.left == None:
                        # Add Node
                        currentNode.left = newNode
                        break
                    else: 
                        # Go Left
                        currentNode = currentNode.left

                else:
                    if currentNode.right == None:
                        # Add Node
                        currentNode.right = newNode
                        break
                    else:
                        # Go right
                        currentNode = currentNode.right

    def lookup(self, value):
        pass
    
    def print_tree(self):
        if self.root != None:
            self.printt(self.root)

    def printt(self,curr_node):
        if curr_node != None:
            self.printt(curr_node.left)
            print(str(curr_node.value))
            self.printt(curr_node.right)

myTree = BinarySearchTree()
myTree.insert(9)
myTree.insert(4)
myTree.insert(6)
myTree.insert(20)
myTree.insert(170)
myTree.insert(15)
myTree.insert(1)
myTree.print_tree()