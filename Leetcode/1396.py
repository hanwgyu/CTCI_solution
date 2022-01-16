class UndergroundSystem:
    def __init__(self):
        self.d = dict()
        self.start = dict()

    def checkIn(self, id: int, startStation: str, t: int) -> None:
        self.start[id] = (startStation, t)

    def checkOut(self, id: int, endStation: str, t: int) -> None:
        startStation, start_t = self.start[id]
        total, n = 0, 0
        if (startStation, endStation) in self.d:
            total, n = self.d[(startStation, endStation)]
        self.d[(startStation, endStation)] = (total+t-start_t, n+1)
        del self.start[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, n = self.d[(startStation, endStation)]
        return total/n
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)