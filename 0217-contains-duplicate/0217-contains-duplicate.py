class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()

        for num in nums:
            nums_set.add(num)

        return len(nums) != len(nums_set)

    def containsDuplicate2(self, nums: List[int]) -> bool:
        nums_set = set()

        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)

        return False

    