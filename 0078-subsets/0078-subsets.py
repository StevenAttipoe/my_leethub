class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #O(N * 2^N) runtime
        #O(N) space 
        ''' The space purposefully used for returning the output is ignored 
            is always ignored in space complexiity analysis'''
        def backtrack(start, sub):
            if start > len(nums):
                return
            
            res.append(list(sub))
            
            for i in range(start, len(nums)):
                sub.append(nums[i])
                backtrack(i + 1, sub)
                sub.pop()

        res = []
        backtrack(0, [])
        return res
        