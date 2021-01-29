class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0: 
            return 0
        elif n==1 or n==2:
            return 1
        seen = {0:0, 1:1, 2:1}
        i = 3
        tribonacci = 0
        while i <= n:
            tribonacci = seen[i-3] + seen[i-2] + seen[i-1]
            seen[i] = tribonacci 
            i+=1
        return tribonacci
