#(()(()))
def maxDepth(s):
    parenthese_list = []
    depth_list = []
    nested_depth = 0
    for i in s:
        if i == '(' or i == ')':
            parenthese_list.append(i)
    for i in parenthese_list:
        if i == '(':
            nested_depth += 1
        else:
            depth_list.append(nested_depth)
            nested_depth -= 1
    return max(depth_list)

