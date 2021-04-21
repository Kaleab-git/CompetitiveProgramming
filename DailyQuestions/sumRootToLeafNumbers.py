# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        que = deque([(root,f"{root.val}")])
        ans = []
        while que:
            node, prefix = que.popleft()
            if not node.left and not node.right: ans.append(prefix)
            for child in [node.left, node.right]:
                if child: que.append((child,prefix+f"{child.val}"))
        return sum(int(num) for num in ans)