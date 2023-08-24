class Solution:
    # O(n⋅n!) runtime
    # O(n) space
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(i):
            if len(nums) == i:
                result.append(nums[:])
                return

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i] #swap
                backtrack(i + 1)
                nums[i], nums[j] = nums[j], nums[i] #swap back

        backtrack(0)
        return result
        