from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Init:
        size = len(s1)

        # setting up target
        target = defaultdict(int)
        for char in s1:
            target[char] += 1

        # setting up window:
        window = defaultdict(int)
        
        for i, char in enumerate(s2):
            # Add:
            window[char] += 1

            # shrink window if too big:
            if i >= size:
                left = s2[i-size]

                # delete dict if zero to maintain match
                window[left] -= 1
                if window[left] == 0:
                    del window[left]
                    
            # check if matching
            if window == target:
                return True

        return False