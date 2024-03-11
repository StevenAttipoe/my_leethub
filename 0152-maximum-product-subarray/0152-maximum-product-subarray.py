class Solution:
    def maxProduct(self, nums: List[int]) -> int: 
        maxSubProduct = max(nums)
        curMin = curMax = 1

        for n in nums:
            vals = (n, curMin * n, curMax * n)
            curMin, curMax = min(vals), max(vals)
            maxSubProduct = max(maxSubProduct, curMax)

        return maxSubProduct

    def maxProduct2(self, nums: List[int]) -> int:        
        N = len(nums)
        maxSubProduct = -math.inf

        for i in range(N):
            subProduct = 1

            for j in range(i, N):
                subProduct *= nums[j]
                maxSubProduct = max(maxSubProduct, subProduct)

        return maxSubProduct

        