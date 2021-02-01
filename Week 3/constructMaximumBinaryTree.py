# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if nums == []:
            return None
        root = TreeNode(max(nums))
        i = nums.index(root.val)
        root.left = self.constructMaximumBinaryTree(nums[:i])
        root.right = self.constructMaximumBinaryTree(nums[i+1:])
        return root 