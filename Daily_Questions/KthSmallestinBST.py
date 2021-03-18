# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import heapq as heap
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not (root.left or root.right):
            return root.val    
        values = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            values.append(node.val)
            for child in [node.left, node.right]:
                if not child: continue
                queue.append(child)
        heap.heapify(values)
        for i in range(k):
            answer = heap.heappop(values)
        return answer