class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        l = 1
        while l <= len(A)-2:
            if A[len(A)-(l+2)] + A[len(A)-(l+1)] > A[len(A)-l]:
                return A[len(A)-(l+2)] + A[len(A)-(l+1)] + A[len(A)-(l)]
            l += 1
        return 0
        
