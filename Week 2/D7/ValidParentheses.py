class Solution(object):
    def isValid(self, s):
        p_dict = {')':'(',']':'[','}':'{'}
        stack = []
        open_p = '{[('
        for i in s:
            if i in open_p:
                stack.append(i)
            elif len(stack) != 0:
                if stack[len(stack)-1] == p_dict[i]:
                    stack.pop() 
                else:
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        return False
                