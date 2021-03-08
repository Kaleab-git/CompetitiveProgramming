class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        max_width = len(height)-1
        left, right = 0, max_width
        for width in range(max_width, 0, -1):
            length = min(height[left], height[right])
            area = max(area, width*length)
            if length == height[left]:
                left += 1
            else:
                right -= 1
        
        return area
            
            
            
            