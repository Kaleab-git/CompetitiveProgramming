class Solution(object):
    def fib(self, n):
        result = 1
        sum = 0
        if n == 0:
            return 0
        elif n == 1:
            return 1
        for i in range(n):
            temp = sum 
            sum = result
            result += temp
        return sum
            