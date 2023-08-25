class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        score = max(nums) - min(nums)

        return score - (2*k) if score > 2 * k else 0