class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count , sum = 0, 0
        d = {0 : 1}
        
        for i in range(len(nums)):
            sum += nums[i]
            dif = sum - k
            if d.get(dif, 0):
                count += d[dif]
            d[sum] = d.get(sum, 0) + 1
        return count
                    
        