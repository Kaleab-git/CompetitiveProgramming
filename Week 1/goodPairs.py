def numIdenticalPairs(self, nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if i < j and nums[j] == nums[i]:
                count += 1
    return count
