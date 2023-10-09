class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        numFreqCount = Counter(arr)
        freqNoOfElementCount = Counter(numFreqCount.values())
        n = len(numFreqCount)

        for num in range(1, len(arr) + 1):
            if k >= num * freqNoOfElementCount[num]:
                k -= num * freqNoOfElementCount[num]
                n -= freqNoOfElementCount[num]
                
            else:
                return n - (k // num)

        return n

    def findLeastNumOfUniqueInts2(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        ans = len(count)

        for frequency in sorted(count.values()):
            k -= frequency

            if k < 0: 
                break

            ans -= 1
        return ans
            
