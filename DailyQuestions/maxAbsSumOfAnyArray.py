class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_sum = max_sum = 0; min_sum = float('inf')
        for num in nums: curr_sum = max(0,curr_sum+num); max_sum = max(curr_sum, max_sum)
        curr_sum = 0 
        for num in nums: curr_sum = min(0,curr_sum+num); min_sum = min(curr_sum, min_sum)
        return max(abs(min_sum),max_sum)
