class UndergroundSystem:

    def __init__(self):
        self.people = {}
        self.station = defaultdict(dict)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.people[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkIn, startStation = self.people[id]
        time = t - checkIn
        if stationName in self.station[startStation]:
            self.station[startStation][stationName].append(time)
        else:
            self.station[startStation][stationName] = [time]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        arr = self.station[startStation][endStation] 
        return sum(arr) / len(arr)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)