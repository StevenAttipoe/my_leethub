class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        negCount = posCount = 0

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                negCount = mid + 1
                left = mid + 1
            else:
                right = mid - 1

        left, right = 0, len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > 0:
                posCount = len(nums) - mid
                right = mid - 1     
            else:
                left = mid + 1

        return max(negCount, posCount)
                   