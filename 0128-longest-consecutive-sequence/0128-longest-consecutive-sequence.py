class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        nums_set = set(nums)

        for n in nums_set:
            if n - 1 not in nums_set:
                num = n
                cur_streak = 1

                while num + 1 in nums_set:
                    cur_streak += 1
                    num += 1
                
                longest_streak = max(longest_streak, cur_streak)
            
        return longest_streak

    def longestConsecutive2(self, nums: List[int]) -> int:
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
        