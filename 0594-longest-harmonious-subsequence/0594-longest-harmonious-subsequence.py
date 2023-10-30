class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = {}
        maxLength = 0

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n in count.keys():
            if n + 1 in count:
                maxLength = max(maxLength, count[n] + count[n + 1])
        
        return maxLength
