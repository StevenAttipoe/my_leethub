class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for interval in intervals:
            # No overlap
            if interval[1] < newInterval[0]:
                res.append(interval)

            # newInterval comes before current interval
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = interval

            # There's an overlap
            elif interval[1] >= newInterval[0] or newInterval[1] >= interval[0]:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        res.append(newInterval)
        return res

            