class UndergroundSystem:

    def __init__(self):
        self.timesheet = {}
        self.stats = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.timesheet[id] = (stationName, t) 

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation , startTime = self.timesheet[id]
        self.timesheet.pop(id)
        
        if (startStation,stationName) in self.stats:
            self.stats[(startStation,stationName)][0] += 1
            self.stats[(startStation,stationName)][1] += t - startTime
        else:
            self.stats[(startStation,stationName)] = [1, t - startTime]


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        numOfTravels, totalTravelTime = self.stats[(startStation, endStation)]
        return totalTravelTime / numOfTravels
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)