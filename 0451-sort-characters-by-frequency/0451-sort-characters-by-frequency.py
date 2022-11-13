class Solution:
    #O(n) time and O(n) space
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        
        buckets = [[] for _ in range(len(s) +1)]
        
        for c,freq in count.items():
            buckets[freq].append(c)
            
        
        sortedChars = []
        for freq in range(len(buckets)-1, -1, -1):
            for j in (buckets[freq]):
                sortedChars.append(freq * j)
                
        return "".join(sortedChars)