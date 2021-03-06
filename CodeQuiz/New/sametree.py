# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        if p or q:
            if p and q:
                if p.val != q.val:
                    return False
                else:
                    return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
        else:
            return True