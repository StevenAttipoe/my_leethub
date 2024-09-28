class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1

        while i < j:
            totalSum = nums[i] + nums[j]

            if totalSum == target:
                return [i + 1, j + 1]
            elif totalSum > target:
                j -= 1
            else:
                i += 1

        return [-1, -1]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i + 1]
            
            seen[nums[i]] = i + 1

        return [-1, -1]