class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        first_sum = {}
        for i in nums1:
            for j in nums2:
                if (i+j) in first_sum: first_sum[i + j] += 1
                else: first_sum[i + j] = 1
        for k in nums3:
            for l in nums4:
                if -(k+l) in first_sum: count += first_sum[-(k+l)]
        return count

        # nums1[i] + nums2[j] + nums3[k] + nums[l] == 0 
        # is means 
        # nums1[i] + nums2[j] = -(nums3[k] + nums[l])
        # first_sum = -(second_sum)