def height(root, lh=0,rh=0):
    if root.left:
        lh += 1
        lh += height(root.left)
    if root.right:
        rh += 1
        rh += height(root.right)
    if lh > rh:
        return lh
    else:
        return rh


# has time complexity of O(n), maybe, n bieng hight of the tree
# has O(n) worst case space complexity. O(log)
#
#
#
#
