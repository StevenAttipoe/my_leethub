class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        pivot = len(nums) - 2
        
        #Find pivot, index of element that is non increasing
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1

        #Find next num greater than pivot num
        if pivot >= 0:
            nxt = len(nums) - 1
            while nxt > 0 and nums[pivot] >= nums[nxt]:
                nxt -= 1
            self.swap(nums, pivot, nxt)

        #Reverse subarray after pivot
        l, r = pivot + 1, len(nums) - 1
        while l < r:
            self.swap(nums, l, r)
            l += 1
            r -= 1

    def swap(self, nums, l, r):
        nums[l], nums[r] = nums[r], nums[l]


        
        