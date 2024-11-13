class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax, rightMax = -1, -1
        totalAmount = 0

        while l < r:
            leftMax = max(leftMax, height[l])
            rightMax = max(rightMax, height[r])

            if leftMax < rightMax:
                totalAmount += leftMax - height[l]
                l += 1
            else:
                totalAmount += rightMax - height[r]
                r -= 1
        
        return totalAmount
        
    def trap2(self, height: List[int]) -> int:
        n = len(height)
        totalAmount = 0

        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        for i in range(n):
            totalAmount += min(leftMax[i], rightMax[i]) - height[i]
        
        return totalAmount


        