class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        best = 0
        unique = set()

        start, end = 0, 0
        while end < len(s):
            while s[end] in unique:
                unique.remove(s[start])
                start += 1

            unique.add(s[end])
            best = max(best, end-start+1)
            end += 1

        return best

        