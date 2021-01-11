class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        while i < len(nums)-1:
            while nums[i] == nums[i+1]:
                nums.remove(nums[i+1])
                if i+1 > len(nums)-1:
                    break
            i+=1
        return len(nums)