def numIdenticalPairs(nums):
    Max = nums[0]
    for i in nums:
        if i > Max:
            Max = i
    counterList = [0] * (Max + 1) 
    pairs = 0
    for i in range(len(nums)): 
        pairs += counterList[nums[i]]
        counterList[nums[i]] += 1
    return pairs 
                
print (numIdenticalPairs([1,2,6,2,1,1,0,1]))