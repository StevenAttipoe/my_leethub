class UndergroundSystem:

    def __init__(self):
        self.timesheet = {}
        self.durations = defaultdict(lambda: [0,0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.timesheet[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        (checkInStation, checkInTime) = self.timesheet.pop(id)
        self.durations[(checkInStation, stationName)][0] += t - checkInTime
        self.durations[(checkInStation, stationName)][1] += 1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, totalTrips = self.durations[(startStation, endStation)]
        return totalTime / totalTrips
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)