class Solution:
    def trap(self, height: List[int]) -> int:
        l , r = 0 , len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        res = 0
        
        while l < r:
            if maxLeft < maxRight:
                l += 1
                amount = maxLeft - height[l]
                if amount > 0:
                    res += amount
                maxLeft = max(maxLeft, height[l])
                
            else:
                r -= 1
                amount = maxRight - height[r]
                if amount > 0:
                    res += amount
                maxRight = max(maxRight, height[r])
        
        return res