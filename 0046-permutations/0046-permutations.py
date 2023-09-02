class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def helper(permutation):
            if len(permutation) == len(nums):
                permutations.append(permutation[:])
                return

            for num in nums:
                if num not in permutation:
                    permutation.append(num)
                    helper(permutation)
                    permutation.pop()

        helper([])
        
        return permutations

        