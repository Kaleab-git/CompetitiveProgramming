# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root:
            if not root.left and not root.right:
                return not bool(targetSum - root.val)    
            leftPath = rightPath = False
            if root.left:
                leftPath = self.hasPathSum(root.left, targetSum - root.val)

            if root.right:
                rightPath = self.hasPathSum(root.right, targetSum - root.val)


            if leftPath or rightPath:
                return True
            else:
                return False
