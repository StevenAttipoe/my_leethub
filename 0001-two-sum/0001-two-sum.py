class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for position, num in enumerate(nums):
            table[num] = position

        
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in table and table[complement] != i:
                return [i, table[complement]]