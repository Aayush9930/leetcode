class UndergroundSystem:

    def __init__(self):
        self.checkInTime = {}
        self.timeTaken = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInTime[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        ci_station, ci_time = self.checkInTime[id]
        if ci_station in self.timeTaken:
            if stationName in self.timeTaken[ci_station]:
                self.timeTaken[ci_station][stationName].append(t - ci_time)
            else:
                self.timeTaken[ci_station][stationName] = [t - ci_time]

        else:
            self.timeTaken[ci_station] = { stationName:[t - ci_time] }
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        avg = sum(self.timeTaken[startStation][endStation]) / len(self.timeTaken[startStation][endStation])
        return avg


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)