class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxStreak = 0

        for n in numsSet:
            if n - 1 not in numsSet:
                curStreak = 0
                curNo = n

                while curNo in numsSet:
                    curStreak += 1
                    curNo += 1

                maxStreak = max(maxStreak, curStreak)

        return maxStreak

    def longestConsecutive2(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        maxStreak = 1
        curStreak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i - 1] + 1 == nums[i]:
                    curStreak += 1
                else:
                    maxStreak = max(maxStreak, curStreak)
                    curStreak = 1     

        return max(maxStreak, curStreak)


        