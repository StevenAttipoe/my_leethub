class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        counts = {}

        for num in nums:
            pairs += counts.get(num, 0)
            counts[num] = counts.get(num, 0) + 1          

        return pairs

        