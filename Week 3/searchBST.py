# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        if root == None:
            return root
        if root.val == val:
            return root
        else:
            if val > root.val:
                return self.searchBST(root.right, val)
            else:
                return self.searchBST(root.left, val)
            