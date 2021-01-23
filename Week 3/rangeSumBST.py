# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        if root:
            left = None; right = None
            if root.left:
                left = root.left
            if root.right:
                right = root.right
            if root.val <= high and root.val >= low:
                return root.val + self.rangeSumBST(right,low,high) + self.rangeSumBST(left,low,high)
            else:
                return self.rangeSumBST(right,low,high) + self.rangeSumBST(left,low,high)
        else:
            return 0 #cause 0  wont affect our addition result. Also dont want to return None and try to add it