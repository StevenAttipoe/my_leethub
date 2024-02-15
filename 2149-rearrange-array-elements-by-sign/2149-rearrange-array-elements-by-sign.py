class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i = j = 0
        res = []

        while i < len(nums) and j < len(nums):
            while nums[i] < 0:
                i += 1

            res.append(nums[i])
            i += 1

            while nums[j] > 0:
                j += 1
            
            res.append(nums[j])
            j += 1
        return res
            


        