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
        dpt = self.dep[id]

        if stationName in self.avgs:
            avgDur, count = self.avgs[stationName].get(dpt, (0, 0))

            self.avgs[stationName][dpt] = ((avgDur*count+timeTaken)/(count+1), count+1)

        else:
            self.avgs[stationName] = {dpt: (timeTaken, 1)}



    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # KEY BY: START AND END STATION
        # Returns; avg duration of ALL completed trips ^matching

        return self.avgs[endStation][startStation][0]

