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
            best = max(best, len(unique))
            end += 1
            
        return best

        # unique = set()
        # best = 0
        # for char in s:
        #     if char in unique:
        #         unique.clear()
        #     unique.add(char)
        #     best = max(best, len(unique))
        # return best

        