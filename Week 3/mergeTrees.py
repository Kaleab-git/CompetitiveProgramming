# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, t1, t2):
        if t2 == None:
            return t1
        elif t1 == None:
            return self.mergeTrees(t2, t1)
        if t1 and t2:
            t1.val+=t2.val
            if t1.right:
                self.mergeTrees(t1.right,t2.right)
            else:
                t1.right = t2.right
            
            if t1.left:
                self.mergeTrees(t1.left,t2.left)
            else:
                t1.left = t2.left    
        return t1
            
        