class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        low, high = nums[0], nums[-1]
        score = high - low

        for i in range(len(nums) - 1):
            a, b = nums[i], nums[i + 1]
            cur_score = max(high - k, a + k) - min(low + k, b - k)
            score = min(score, cur_score)

        return score