class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        count = sorted(count.items(), key = lambda x:x[1])
        
        sorted_arr = []
        for num, freq in count:
            for i in range(freq):
                sorted_arr.append(num)
        
        res = 0
        seen = set()
        for val in sorted_arr:
            if k:
                k -= 1
                continue

            if val not in seen:
                seen.add(val)
                res += 1

        return res

            
