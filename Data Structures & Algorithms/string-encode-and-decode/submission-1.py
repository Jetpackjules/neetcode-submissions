class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for string in strs:
            out += str(len(string))+'#'+string
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            num = ""
            while s[i] != "#":
                num+=s[i]
                i+=1
            i+=1
            out.append(s[i:i+int(num)])
            i += int(num)
        return out

                

            
