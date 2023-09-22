class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0
        while l < r:
            if height[l] < height[r]:
                area = height[l] * (r - l)
                l += 1
            else:
                area = height[r] * (r - l)
                r -= 1
            maxArea = max(maxArea, area)
        return maxArea

        
        