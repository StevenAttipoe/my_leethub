class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pairs = []

        for a in range(len(numbers)):
            b = self.search(a, target, numbers)
            print(a, b)
            if b != None and a !=b:
                return [a + 1, b + 1]

    def search(self, a, target, nums):
        l = a
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if a == mid:
                mid += 1
            if nums[a] + nums[mid] < target:
                l = mid + 1
            elif nums[a] + nums[mid] > target:
                r = mid - 1
            else:
                return mid

        return None

        
        