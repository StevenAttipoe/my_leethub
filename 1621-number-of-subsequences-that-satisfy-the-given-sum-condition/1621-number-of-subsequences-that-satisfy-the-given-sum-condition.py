class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        nums.sort()
        mod, count = 10 ** 9 + 7, 0

        while l <= r:
            if nums[l] + nums[r] <= target:
                count = (count + pow(2, r - l, mod)) % mod
                l += 1
            else:
                r -= 1
        return count

        