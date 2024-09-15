class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])

        rooms = []
        heapq.heappush(rooms, (intervals[0][1], intervals[0]))

        for i in intervals[1:]:
            if rooms[0][1][1] <= i[0]:
                heapq.heappop(rooms)

            heapq.heappush(rooms, (i[1], i))

        return len(rooms)