# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = deque([(root,1)])
        left_most = (root.val,0)#(node.val, depth)
        while queue:
            node, depth = queue.popleft()
            
            for child in [node.left, node.right]:
                if not child: continue
                if depth+1 > left_most[1]: left_most = (child.val, depth+1)
                print (left_most)
                queue.append((child, depth+1))
        
        return left_most[0]