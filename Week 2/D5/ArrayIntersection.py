class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = list(set(nums1))
        nums1.sort()
        nums2 = list(set(nums2))
        nums2.sort()
        intersection = []

        for i in nums1:
            for j in nums2:
                if i == j:
                    intersection.append(i)
                elif j > i:
                    break
        return intersection
