class Solution(object):
    def checkPossibility(self, nums):
        if len(nums) < 3 or nums == sorted(nums):
            return True
        iThatFails = -1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if iThatFails == -1:
                    iThatFails = i
                else:
                    return False  
        array1 = []; array2 = []
        for i in range(len(nums)):
            if i == iThatFails:
                array2.append(nums[i])
                continue
            elif i == iThatFails+1:
                array1.append(nums[i])
                continue
            else:
                array1.append(nums[i])
                array2.append(nums[i])
        if array1 == sorted(array1) or array2 == sorted(array2):
            return True
        return False