import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        total = sum(nums)
        l = 1; result = r = max(nums)
        while l<=r:
            mid = (l+r)//2 #mid btw is the divisor
            Sum = math.ceil(total/mid)  
            if Sum > threshold:
                l = mid+1
            else:
                if result > mid:
                    result = mid
                r = mid-1

        return result

    def getSum(self, nums, d):
        Sum = 0
        for i in range(len(nums)):
            Sum += math.ceil(nums[i]/d)
        return Sum        