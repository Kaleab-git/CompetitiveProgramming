# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        inserted = False
        node = root
        if node:
            while inserted == False:
                if node.val < val:   # we're concerned with right side in this case
                    if node.right:
                        node = node.right
                    else:
                        node.right = TreeNode(val)
                        inserted = True 
                else:  # left side in this case
                    if node.left:
                        node = node.left
                    else:
                        node.left = TreeNode(val)
                        inserted = True
            return root
        else:
            return TreeNode(val)