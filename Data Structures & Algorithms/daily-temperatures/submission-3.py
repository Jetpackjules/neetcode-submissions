class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack of all the RELEVANT ONES
        # popped out of the stack when biger temp is found
        # seperate stack of indexes? maybe tuple stack?

        idxStack = []
        for idx, temp in enumerate(temperatures):
            while idxStack and temperatures[idxStack[-1]] < temp:
                smolIdx = idxStack.pop()
                temperatures[smolIdx] = idx-smolIdx
            idxStack.append(idx)

        for idx in idxStack:
            temperatures[idx] = 0
        return temperatures