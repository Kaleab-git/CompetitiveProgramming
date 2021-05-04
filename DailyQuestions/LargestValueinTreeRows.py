from collections import deque
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []
        que = deque([(root, 0)]); ans = [(root,0)]; level = 0
        while que:
            node, depth = que.popleft()
            if level!=depth:
                if que: ans.append(max(max(que, key=lambda x:x[0].val),(node,depth),key=lambda x:x[0].val))
                else: ans.append((node,depth))
                level = depth
            for child in [node.left, node.right]:
                if child: que.append((child, depth+1))
        return [x[0].val for x in ans]
