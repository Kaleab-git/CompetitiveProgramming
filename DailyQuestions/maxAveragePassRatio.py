import heapq as hp
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap=[(-((p+1)/(t+1)-(p/t)),p,t) if p!=t else (0,p,t) for p,t in classes]
        hp.heapify(heap)
        for _ in range(extraStudents):
            change, p,t = hp.heappop(heap)
            hp.heappush(heap,(-(((p+2)/(t+2))-((p+1)/(t+1))), p+1, t+1)) 
        Sum = 0
        for _,p,t in heap: Sum += (p/t)
        return Sum/len(classes)