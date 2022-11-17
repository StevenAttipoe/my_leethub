class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        _sum = sum(nums)
        leftMostSum = 0
        
        for i, num in enumerate(nums):
            if leftMostSum == (_sum - num - leftMostSum):
                return i
            leftMostSum += num
            
        return -1
        