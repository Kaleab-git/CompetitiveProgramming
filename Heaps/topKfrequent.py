class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        countDict = {}
        for num in nums:
            if num in countDict:
                countDict[num] += 1
            else:
                countDict[num] = 1
        print (countDict)
        countDict = dict(sorted(countDict.items(),reverse=True, key = lambda x: x[1]))
        answer = []
        i=0
        for num in countDict:
            print (i, k)
            if i == k:
                return answer
            answer.append(num)
            i += 1
        return answer