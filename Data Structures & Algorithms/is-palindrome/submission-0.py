class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        
        s = [char for char in s.lower() if char.isalnum()]
        j = len(s)-1
        # print(s)

        while i < j:
            if s[i] != s[j]:
                # print(s[i], s[j])
                return False
            else:
                i+=1
                j-=1
        return True