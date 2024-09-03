class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for k, v in count.items():
            if v == 1:
                return k