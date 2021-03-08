import heapq as heap


class Solution(object):
    def lastStoneWeight(self, stones):
        myHeap = []
        for stone in stones:
            heap.heappush(myHeap, -stone)

        while len(myHeap) > 1:
            y = -heap.heappop(myHeap)
            x = -heap.heappop(myHeap)
            if x != y:
                heap.heappush(myHeap, x-y)

        if len(myHeap) == 0:
            return 0
        else:
            return -myHeap[0]
