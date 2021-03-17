# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = deque([(root, 1)])
        level = 1
        level_list = []
        answer = []
        reverse = False
        while queue:
            node, depth = queue.popleft()
            if not node: return []
            if depth == level:
                level_list.append(node.val)
            else:
                level += 1
                if reverse:
                    level_list = level_list[::-1]
                    reverse = False
                else:
                    reverse = True
                answer.append(level_list)
                level_list = [node.val]
            for child in [node.left, node.right]:
                if not child: continue
                queue.append((child, depth+1))
        if level_list:
            if reverse:
                level_list = level_list[::-1]
            answer.append(level_list)

        return answer
    
    
    