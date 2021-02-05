import heapq as heap

class Solution(object):
    def topKFrequent(self, nums, k):
        countDict = {}
        myHeap = []
        for num in nums:
            if num in countDict:
                countDict[num] += 1
            else:
                countDict[num] = 0
                
        for i in countDict:
            heap.heappush(myHeap, -countDict[i])
        
        answer = []
        frequencyList = countDict.values()
        numList = countDict.keys()
        
        for i in range(1,k):
            answer.append(numList[frequencyList.index(i)])

        return answer

        
solution  = Solution()

print (solution.topKFrequent([1,1,1,2,2,3], 2))