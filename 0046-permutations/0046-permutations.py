class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def helper(i):
            if i == len(nums):
                permutations.append(nums[:])
                return

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                helper(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        helper(0)
        
        return permutations

        