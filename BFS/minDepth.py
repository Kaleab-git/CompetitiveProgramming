# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue = deque([(root, 1)])#initialize deque with a list of tuples of node and associated depth
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right: return depth #BFS guarentees that the first time we reach a node is the fastest way to reach it. So the first leaf we encounter is has the minimum depth 
            for child in [node.left, node.right]: #for each node iterate through a list of it's 2 children
                if not child: continue 
                queue.append((child, depth+1))#cause we fetched the parent depth and we're @child
        