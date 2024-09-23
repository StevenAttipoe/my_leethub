class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

            if freq[n] > len(nums) // 2:
                return n
        