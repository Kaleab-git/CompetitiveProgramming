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


