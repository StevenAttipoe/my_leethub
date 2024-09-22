class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while nums[i] >= nums[j]:
                j -= 1
            self.swap(i, j, nums)
        
        self.reverse(i + 1, nums)
    
    def swap(self, i, j, nums):
        nums[i], nums[j] = nums[j], nums[i]
    
    def reverse(self, s, nums):
        e = len(nums) - 1

        while s < e:
            self.swap(s, e, nums)
            s += 1
            e -= 1

            

        