class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort(key = lambda x: "".join(sorted((x))))
        print(strs)
        
        out = [[]]
        out[-1].append(strs[0])
        
        for word in strs[1:]:
            if "".join(sorted((word))) == "".join(sorted((out[-1][-1]))):
                out[-1].append(word)
            else:
                out.append([word])
        return out
