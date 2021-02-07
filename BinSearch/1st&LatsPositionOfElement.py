class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.position = []
        self.started = False
        length = len(nums)
        for i in range(length):
            if nums[i] == target and not self.started:
                self.started = True
                self.position.append(i)
            elif nums[i] != target and self.started:
                self.position.append(i-1)
                return self.position
        if self.started:
            self.position.append(length-1)
            return self.position
        else:
            return [-1,-1]