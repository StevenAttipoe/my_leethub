class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        ans = len(count)

        for frequency in sorted(count.values()):
            k -= frequency

            if k < 0: 
                break

            ans -= 1
        return ans
            
