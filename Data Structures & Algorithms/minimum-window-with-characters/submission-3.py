class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window:
        
        # grow: until all chars in t are present in s!

        # shrink: until NOT all chars in t are present in s!


        # return smallest sub or 0

        # setup: two dicts, oe for window one for target!

        target = defaultdict(int)
        for char in t:
            target[char] += 1
        tCheck = set(t)

        window = defaultdict(int)
        best = ""
        tail = 0
        curr = 0
        exp = len(t)

        for i, char in enumerate(s):
            if char in target:
                window[char] += 1
                if window[char] <= target[char]:
                    curr += 1

            # while in valid state!
            while exp == curr:
                if (i-tail) < len(best) or best == "":
                    best = s[tail:i+1]

                # update window: remove char count if in target, del for comp
                if s[tail] in window:
                    window[s[tail]] -= 1
                    if window[s[tail]] < target[s[tail]]:
                        curr -= 1
                
                tail += 1
            
        return best

