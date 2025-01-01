class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()

        cur_streak = 1
        longest_streak = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                pass
            elif nums[i] - nums[i - 1] != 1:
                longest_streak = max(longest_streak, cur_streak)
                cur_streak = 1
            else:
                cur_streak += 1
                
        return max(longest_streak, cur_streak)
        