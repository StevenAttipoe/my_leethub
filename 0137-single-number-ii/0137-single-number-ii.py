class Solution:
    # O(n) time and space 
    def singleNumber(self, nums: List[int]) -> int:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for k, v in count.items():
            if v == 1:
                return k

    # O(nlogn) time and O(n) space 
    def singleNumber2(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(0, len(nums) - 1, 3):
            if nums[i] == nums[i + 1]:
                continue
            else:
                return nums[i]

        return nums[-1]

