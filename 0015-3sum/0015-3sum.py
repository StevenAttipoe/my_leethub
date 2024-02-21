class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        distinctTriplets = set()        
        
        for i in range(len(nums) - 2):
            l, r  = i + 1, len(nums) - 1
        
            while l < r:
                _sum = nums[i] + nums[l] + nums[r]
                if _sum == 0:
                    distinctTriplets.add((nums[i], nums[l], nums[r]))
                    r -= 1
                    l += 1
                    
                if _sum > 0:
                    r -= 1
                    
                if _sum < 0:
                    l += 1
        return list(distinctTriplets)
         