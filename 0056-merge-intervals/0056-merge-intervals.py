class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])
        mergedIntervals = [intervals[0]]
        
        for interval in intervals:

            if interval[0] > mergedIntervals[-1][1]:
                mergedIntervals.append(interval)
                
            else:
                mergedIntervals[-1][1] = max(interval[1], mergedIntervals[-1][1])
                
        return mergedIntervals