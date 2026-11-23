class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []

        if not intervals:
            return out

        intervals.sort()

        pStart = intervals[0][0]
        pEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start <= pEnd:
                pEnd = max(end, pEnd)
            
            else:
                out.append([pStart, pEnd])
                pStart = start
                pEnd = end

        out.append([pStart, pEnd])
        
        return out
                