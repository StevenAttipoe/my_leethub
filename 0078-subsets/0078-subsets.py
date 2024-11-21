class Solution:
    # O(N * 2^N) time
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerSet = []

        def backtrack(i, listSet):
            powerSet.append(listSet[:])
            
            for i in range(i, len(nums)):
                listSet.append(nums[i])
                backtrack(i + 1, listSet)
                listSet.pop()

        backtrack(0, [])

        return powerSet
        
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        powerSet = []

        def backtrack(i, listSet):
            powerSet.append(listSet)
            
            for i in range(i, len(nums)):
                backtrack(i + 1, listSet + [nums[i]])

        backtrack(0, [])

        return powerSet
        