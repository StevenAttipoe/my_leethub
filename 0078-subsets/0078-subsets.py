class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerSet = []

        def backtrack(i, listSet):
            powerSet.append(listSet)
            
            for i in range(i, len(nums)):
                backtrack(i + 1, listSet + [nums[i]])

        backtrack(0, [])

        return powerSet
        