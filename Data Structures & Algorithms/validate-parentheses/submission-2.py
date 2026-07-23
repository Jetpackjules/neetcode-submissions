class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        guide = {')': '(', ']': '[', '}': '{'}

        for char in s:
            print(stack, char)
            if char not in guide:
                stack.append(char)
            else:
                if not stack or stack.pop() != guide[char]:
                    return False
        return True if stack == [] else False
        