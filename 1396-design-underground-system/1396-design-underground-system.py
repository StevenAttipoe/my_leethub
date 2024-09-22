class UndergroundSystem:

    def __init__(self):
        self.timesheet = {}
        self.durations = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.timesheet[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        (checkInStation, checkInTime) = self.timesheet[id]
        duration =  t - checkInTime
        self.durations[(checkInStation, stationName)].append(duration)
        del self.timesheet[id]
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        durations = self.durations[(startStation, endStation)]
        return sum(durations) / len(durations)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)