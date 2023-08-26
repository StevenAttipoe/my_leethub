class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        streak = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                cur_streak = 1
                cur_num = num

                while cur_num + 1 in nums_set:
                    cur_num += 1
                    cur_streak += 1

                streak = max(streak, cur_streak)

        return streak