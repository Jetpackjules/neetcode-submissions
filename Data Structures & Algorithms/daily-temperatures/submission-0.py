class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack of all the RELEVANT ONES
        # popped out of the stack when biger temp is found
        # seperate stack of indexes? maybe tuple stack?

        tempStack = []
        idxStack = []
        for idx, temp in enumerate(temperatures):
            while tempStack and tempStack[-1] < temp:
                smol = tempStack.pop()
                smolIdx = idxStack.pop()
                temperatures[smolIdx] = idx-smolIdx

            tempStack.append(temp)
            idxStack.append(idx)
            
        for idx in idxStack:
            temperatures[idx] = 0
        return temperatures