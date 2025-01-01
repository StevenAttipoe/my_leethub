class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            maxArea = max(maxArea, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea
    
    def maxArea2(self, height: List[int]) -> int:
        maxArea = 0
        n = len(height)

        for i in range(n):
            for j in range(i + 1, n):
                area = min(height[i], height[j]) * (j - i)
                maxArea = max(maxArea, area)
        
        return maxArea





        