class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key = lambda x: x[0])
        merged = []

        for i in intervals:
            if not merged or not self.isMergable(merged[-1], i):
                merged.append(i)
            else:
                merged[-1][1] = max(merged[-1][1], i[1])
                
        return merged
    
    def isMergable(self, intervals1, intervals2):
        return intervals1[1] >= intervals2[0]

        