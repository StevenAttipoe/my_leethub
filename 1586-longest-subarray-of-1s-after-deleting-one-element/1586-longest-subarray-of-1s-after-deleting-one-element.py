class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = 0
        ones = 0
        start = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1

            while zeros >= 2:
                if nums[start] == 0:
                    zeros -= 1
                start += 1

            ones = max(ones, i - start)

        return ones