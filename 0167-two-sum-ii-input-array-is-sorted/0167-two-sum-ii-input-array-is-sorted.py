class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1

        return [-1, -1]

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        pairs = []

        for a in range(len(numbers)):
            b = self.search(a, target, numbers)
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

        
        