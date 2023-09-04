class Solution:
    #O(n + k) runtime
    def sortArray(self, nums: List[int]) -> List[int]:
        minVal, maxVal = min(nums), max(nums)
        counts = {}
        index = 0

        for val in nums:
            counts[val] = counts.get(val, 0) + 1

        for k in range(minVal, maxVal + 1, 1):
            while counts.get(k, 0) > 0:
                nums[index] = k
                counts[k] -= 1
                index += 1

        return nums

        