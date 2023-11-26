class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for n in range(len(nums) + 1):
            if n not in nums_set:
                return n
        return -1
        