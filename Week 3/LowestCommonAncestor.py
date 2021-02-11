class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < q.val:
            return self.helper(root, p, q)
        else:
            return self.helper(root, q, p)
            
    def helper(self, root, p, q):
        if root:
            while not (p.val <= root.val <= q.val):
                if p.val > root.val:
                    root = root.right
                elif q.val < root.val:
                    root = root.left
        return root
