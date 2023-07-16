class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        no_of_intervals = 0
        prevEnd = -inf

        for start, end in intervals:
            if start >= prevEnd: #If there is no overlap
                prevEnd = end
            else:
                no_of_intervals += 1
                
        return no_of_intervals

