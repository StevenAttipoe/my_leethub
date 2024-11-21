class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        powerSet = []

        def backtrack(s, listSet):
            powerSet.append(listSet[:])
            
            for i in range(s, len(nums)):
                if i > s and nums[i] == nums[i - 1]:
                    continue

                listSet.append(nums[i])
                backtrack(i + 1, listSet)
                listSet.pop()

        backtrack(0, [])

        return powerSet