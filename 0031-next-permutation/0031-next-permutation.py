class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        pivot = len(nums) - 2

        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1

        if pivot >= 0:
            nxt = len(nums) - 1
            while nxt > 0 and nums[pivot] >= nums[nxt]:
                nxt -= 1

            nums[pivot], nums[nxt] = nums[nxt], nums[pivot]

        l, r = pivot + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


        
        