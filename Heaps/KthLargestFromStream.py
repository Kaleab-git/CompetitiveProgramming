import heapq as hp
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.myHeap = []
        for i in range(min(k, len(nums))):
            hp.heappush(self.myHeap, nums[i])
        for i in range(k, len(nums)):
            self.add(nums[i])
            
    def add(self, val: int) -> int:
        if len(self.myHeap) == self.k and val > self.myHeap[0]:
            hp.heappop(self.myHeap)
            hp.heappush(self.myHeap, val) 
        elif len(self.myHeap) < self.k:
            hp.heappush(self.myHeap, val)
        return self.myHeap[0]