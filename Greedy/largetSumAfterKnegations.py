import heapq as heap
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heap.heapify(A)
        for i in range(K):
            heap.heapreplace(A, -A[0])
        return sum(A)