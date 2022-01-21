class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class ListNode:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
            newNode = Node(value)
            if self.head == None:
                self.head = newNode
                self.tail = self.head
                self.length += 1
            else:
                self.tail.next = newNode
                self.tail = newNode
                self.length += 1

class Solution:
    def reverseBetween(self, head, left, right):
        if left == right:
            return head
        prev_pivot = None
        cur_node = head
        right_node = None
        # 3 --> 5
        # cur_node = 3
        # prev_pivot = None
        index = 1
        while index != left:
            prev_pivot = cur_node
            cur_node = cur_node.next
            index += 1
        # cur_node = 3
        # prev_pivot = None
        length = 0
        left_node = cur_node
        # left_node = 3
        while length != right - left +1:
            tmp = cur_node.next
            cur_node.next = right_node
            right_node = cur_node
            cur_node = tmp
            length += 1
        # cur_node = None
        # left_node(3) --> cur_node(None)
        left_node.next = cur_node
        # prev_pivot(None) --> right_node(5)
        if prev_pivot:
            prev_pivot.next = right_node
        else:
            head = right_node
        print("hello")
        

mySolution = Solution()

myLL = ListNode()
myLL.append(1)
myLL.append(2)
myLL.append(3)
myLL.append(4)
myLL.append(5)
left = 2
right = 4
print(mySolution.reverseBetween(myLL.head, left, right))

myLL = ListNode()
myLL.append(3)
myLL.append(5)
left = 1
right = 2
print(mySolution.reverseBetween(myLL.head, left, right))