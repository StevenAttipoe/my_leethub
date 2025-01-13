class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        n = 0
        k = -math.inf

        for start, end in intervals:
            if start >= k:
                k = end
            else:
                n += 1
        
        return n
        