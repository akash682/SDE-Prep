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
        if self.root is None:
            print("This is an empty BST.")
        else:
            currentNode = self.root
            while True:
                if value == currentNode.value:
                    return True
                elif value < currentNode.value:
                    if currentNode.left == None:
                        return False
                    else: 
                        # Go Left
                        currentNode = currentNode.left
                else:
                    if currentNode.right == None:
                        return False
                    else:
                        # Go right
                        currentNode = currentNode.right
    
    def remove(self, value):
        if self.root is None:
            print("This is an empty BST.")
        else:
            currentNode = self.root
            parentNode = None
            while True:
                if value == currentNode.value:
                    break
                elif value < currentNode.value:
                    if currentNode.left == None:
                        return False
                    else: 
                        # Go Left
                        parentNode = currentNode
                        currentNode = currentNode.left
                else:
                    if currentNode.right == None:
                        return False
                    else:
                        # Go right
                        parentNode = currentNode
                        currentNode = currentNode.right

            

            if currentNode.right.left is None:
                minNode = currentNode.right
                minNode.right = None
                minNode.left = currentNode.left
                parentNode.left = minNode
            else:
                minNode = currentNode.right
                while True:
                    if minNode.left is None:
                        break
                    else:
                        minpar = minNode
                        minNode = minNode.left
                
                minNode.left = currentNode.left
                minNode.right = currentNode.right
                parentNode.left = minNode

    def print_tree(self):
        if self.root != None:
            self.printt(self.root)

    def printt(self,curr_node):
        if curr_node != None:
            self.printt(curr_node.left)
            print(str(curr_node.value))
            self.printt(curr_node.right)

    def breadthFirstSearch(self):
        currentNode = self.root
        list = []
        queue = []
        queue.append(currentNode)

        while len(queue) > 0:
            currentNode = queue.pop(0)
            list.append(currentNode.value)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        return list

    def breadthFirstSearchR(self, queue, list):
        if(len(queue) == 0):
            return list
        currentNode = queue.pop(0)
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
        
        return self.breadthFirstSearchR(queue, list)
    
    def DFSInorder(self):
        return self.traverseInOrder(self.root, [])
    
    def DFSPostorder(self):
        return self.traversePostOrder(self.root, [])

    def DFSPreorder(self):
        return self.traversePreOrder(self.root, [])

    def traverseInOrder(self, node, list):
        if(node.left):
            self.traverseInOrder(node.left, list)
        list.append(node.value)
        if(node.right):
            self.traverseInOrder(node.right, list)
        
        return list

    def traversePreOrder(self, node, list):
        list.append(node.value)
        if(node.left):
            self.traversePreOrder(node.left, list)
        if(node.right):
            self.traversePreOrder(node.right, list)       
        return list
    
    def traversePostOrder(self, node, list):
        if(node.left):
            self.traversePostOrder(node.left, list)
        if(node.right):
            self.traversePostOrder(node.right, list)  
        list.append(node.value)
        return list

    

myTree = BinarySearchTree()
myTree.insert(9)
myTree.insert(4)
myTree.insert(6)
myTree.insert(20)
myTree.insert(170)
myTree.insert(15)
myTree.insert(1)

myTree.lookup(20)
# myTree.remove(4)
# print(myTree.breadthFirstSearch())
# print(myTree.breadthFirstSearchR([myTree.root],[]))

print(myTree.DFSInorder())
print(myTree.DFSPreorder())
print(myTree.DFSPostorder())

"""
DFS
InOrder - [ 1, 4, 6, 9, 15, 20, 170]
Preorder - [9, 4, 1, 6, 20, 15, 170]
PostOrder - [1, 6, 4, 15, 170, 20, 9]

   9
  4 20
1 6 15 170
"""