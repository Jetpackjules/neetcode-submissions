class UndergroundSystem:
    def __init__(self):
        self.time = {}
        self.dep = {}
        self.avgs = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.time[id] = t
        self.dep[id] = stationName
        
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # self.arr[stationName] = self.arr.get(stationName,[])+[t]
        timeTaken = t-self.time[id]
        if stationName in self.avgs:
            tracked = self.avgs[stationName].get(self.dep[id], (0, 0))
            ((tracked[0]*tracked[1]+timeTaken)/(tracked[1]+1), tracked[1]+1)
            self.avgs[stationName][self.dep[id]] = ((tracked[0]*tracked[1]+timeTaken)/(tracked[1]+1), tracked[1]+1)

        else:
            self.avgs[stationName] = {self.dep[id]: (timeTaken, 1)}



    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # KEY BY: START AND END STATION
        # Returns; avg duration of ALL completed trips ^matching

        return self.avgs[endStation][startStation][0]

