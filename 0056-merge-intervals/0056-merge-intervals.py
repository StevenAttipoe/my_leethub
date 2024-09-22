class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key = lambda x: x[0])
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            if self.isMergable(merged[-1], intervals[i]):
                startInterval = merged.pop()
                merged.append(self.mergeIntervals(startInterval, intervals[i]))
            else:
                merged.append(intervals[i])

        return merged
    
    def isMergable(self, intervals1, intervals2):
        return intervals1[1] >= intervals2[0]

    def mergeIntervals(self, intervals1, intervals2):
        return [intervals1[0], max(intervals1[1], intervals2[1])]

        