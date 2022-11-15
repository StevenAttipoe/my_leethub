class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        windowSum = 0
        minSize = float("inf")
        
        for r in range(len(nums)):
            windowSum += nums[r]
            
            while windowSum >= target:
                minSize = min(minSize, r - l + 1)
                windowSum -= nums[l]
                l += 1
                
        return 0 if minSize == float("inf") else minSize
        