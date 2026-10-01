from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding window:
        # slide a fixed size window of the len of the s1

        # edge cases:
        # s1 bigger than s2: return false
        # s1 empty: return true
        
        if len(s1) > len(s2):
            return False
        elif not s1:
            return True


        size =len(s1)
        i = 0

        target = defaultdict(int)
        for c in s1:
            target[c] += 1

        dic = defaultdict(int) 
        

        while i < len(s2):
            sub = s2[i-size:i]
            dic[s2[i]] += 1
            

            if i >= size:
                print("CCEHCKING:", dic, target)
                dic[s2[i-size]] -= 1
                if dic[s2[i-size]] == 0:
                    del dic[s2[i-size]]


            # check if they match:
            if dic == target:
                return True
                
            # we need to figure out if sub is a permutaiton! 
            # permuation: has the same amount of chars of each char (lol)
            # solution: dict! that changes every new char since quicker than recomp!
            print(dic)
            i += 1


        return False
        
        