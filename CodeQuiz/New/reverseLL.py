class Solution:
    def reverseList(self, head):
        cur_node = self.head
        prev_node = None
        while cur_node != None:
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = cur_node.next
        