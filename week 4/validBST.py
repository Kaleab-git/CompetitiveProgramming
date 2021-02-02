# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root, Min=-2147483649, Max=2147483648):
        if root:
            if Min < root.val < Max:
                return self.isValidBST(root.right, root.val, Max) and self.isValidBST(root.left, Min, root.val)
            return False
        return True