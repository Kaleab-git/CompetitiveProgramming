# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        answer = []
        if root:
            answer = self.postorderTraversal(root.left)
            answer += self.postorderTraversal(root.right)
            answer.append(root.val)
        answer.append('null')    
        return answer
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        pot1 = self.postorderTraversal(p)
        pot2 = self.postorderTraversal(q)
        print (pot1, pot2)
        if pot1 == pot2:
            return True
        else:
            return False
        
