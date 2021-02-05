def sum_digits(n,k):
    summation = 0
    for i in n:
        summation += int(i)
    return str(summation * k)

# Complete the superDigit function below.
def superDigit(n, k):
    while len(n) > 1:
        n = sum_digits(n,k)
        k = 1
    return n
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


