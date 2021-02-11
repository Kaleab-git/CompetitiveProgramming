# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.array = []
        self.array = self.inOrder(root, self.array)
        min = 10**5
        for i in range(len(self.array)-1):
            if self.array[i+1] - self.array[i] < min:
                min = self.array[i+1] - self.array[i]
        return min
            
    
    
    def inOrder(self, root, array):
        if root:
            self.inOrder(root.left, array)
            array.append(root.val)
            self.inOrder(root.right, array)
        return array    
        
    
    
    
    def compare(self, root, gMin):
        if abs(self.goRight(root.left)):
            print ()
    
    def goLeft(self, root):
        if root.left and root.left.left:
            return self.goLeft(root.left)
        return self.goRight(root.right)
    def goRight(self, root):
        if root.right and root.right.right:
            return self.goRight(root.right)
        return 