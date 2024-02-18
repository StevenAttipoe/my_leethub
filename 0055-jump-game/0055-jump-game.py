class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nextToLast = len(nums) - 1
        currentStep = nextToLast

        for index in range(len(nums) - 2, -1, -1):
            if index + nums[index] >= currentStep:
                currentStep = index

        return currentStep == 0