class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        streak = 1
        cur_streak = 1

        for i in range(len(nums) - 1):
            if nums[i + 1] != nums[i]:
                if nums[i] + 1 == nums[i + 1]:
                    cur_streak += 1
                else:
                    streak = max(streak, cur_streak)
                    cur_streak = 1

        return max(streak, cur_streak)

        
        