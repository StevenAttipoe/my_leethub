class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numFreq = {}

        for num in nums:
            numFreq[num] = numFreq.get(num, 0) + 1

            if len(numFreq) <= 2:
                continue
            
            newNumFreq = {}
            for n, f in numFreq.items():
                if f > 1:
                    newNumFreq[n] = f - 1
            numFreq = newNumFreq
        
        result = []
        for n in numFreq:
            if nums.count(n) > len(nums) // 3:
                result.append(n)

        return result

    def majorityElement2(self, nums: List[int]) -> List[int]:
        numFreq = {}
        n = len(nums)

        for num in nums:
            numFreq[num] = numFreq.get(num, 0) + 1
        
        result = []
        for k in numFreq.keys():
            if numFreq[k] > (n // 3):
                result.append(k)
        
        return result
        