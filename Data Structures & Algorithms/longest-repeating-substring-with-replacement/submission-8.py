import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1 or k >= len(s):
            return len(s)
        
        counts = defaultdict(int)

        start = 0
        end = 1
        com = s[0]
        counts[com] += 1
        other = 0
        lon = 1

        while end < len(s):
            counts[s[end]]+=1
            if s[end] != com:
                other += 1
                if counts[s[end]] > counts[com]:
                    other += counts[com]
                    com = s[end]
                    other -= counts[com]

            if other > k:
                counts[s[start]] -= 1
                if s[start] != com:
                    other -= 1
                start += 1

            lon = max(lon, end-start+1)
            end+=1
            


        return lon
        