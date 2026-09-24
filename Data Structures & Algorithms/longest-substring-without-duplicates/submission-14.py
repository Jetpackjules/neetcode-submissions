class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Slidig window:
        # Move front, until hit a dupe.
        # how to check for dupe: set? o(n) space, still o(n) runitme tho

        if len(s) <= 1:
            return len(s)


        window = set()
        window.add(s[0])

        back = 0
        front = 1
        lon = 0
        
        while front < len(s):
            while s[front] in window:
                window.remove(s[back])
                back += 1

            window.add(s[front])       
            lon = max(len(window), lon)

            front += 1

        return lon