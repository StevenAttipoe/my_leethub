class Solution:
    #O(n ^ 2) time
    def lengthOfLIS(self, nums: List[int]) -> int:
        LEN = len(nums)
        LIS = [1] * LEN

        for i in range(LEN - 1, -1, -1):
            for j in range(i, LEN):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)
                
        