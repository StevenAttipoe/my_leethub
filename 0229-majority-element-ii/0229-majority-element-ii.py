class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numFreq = {}
        n = len(nums)

        for num in nums:
            numFreq[num] = numFreq.get(num, 0) + 1
        
        result = []
        for k in numFreq.keys():
            if numFreq[k] > (n // 3):
                result.append(k)
        
        return result
        