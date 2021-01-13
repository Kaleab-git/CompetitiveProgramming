class Solution(object):
    def fib(self, n):
        result = 1
        sum = 0
        if n == 0:
            return 0
        for i in range(n-1):
            temp = sum
            sum = result
            result += temp
        return result

s = Solution()
for i in range(7):
    print(s.fib(i),end = " ")