class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, sub):
            if start > len(nums):
                return

            res.append(list(sub))

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                sub.append(nums[i])
                backtrack(i + 1, sub)
                sub.pop()
          
        res = []
        nums.sort()
        backtrack(0, [])
        return res



        