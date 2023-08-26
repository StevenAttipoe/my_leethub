class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        concat = [None for i in range(n * 2)]

        for i in range(n):
            concat[i] = concat[i + n] = nums[i]

        return concat