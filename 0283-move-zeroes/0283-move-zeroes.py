class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
                
        p = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[p] = nums[i]
                p += 1

        for i in range(p, len(nums)):
            nums[i] = 0
            
        