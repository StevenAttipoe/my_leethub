class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l , r = 0, len(nums) - 1 

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] == target:
                if nums[l]!= target:
                    l += 1
                if nums[r] != target:
                    r -= 1
                if nums[l] == target and nums[r] == target:
                    return [l, r]
        return [-1, -1]