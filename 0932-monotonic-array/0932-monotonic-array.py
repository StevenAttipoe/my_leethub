class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        sign = 1 if nums[0] <= nums[-1] else -1

        for i in range(len(nums) - 1):
            if sign == 1 and nums[i] > nums[i + 1]:
                return False
            elif sign == -1 and nums[i] < nums[i + 1]:
                return False
        return True

        