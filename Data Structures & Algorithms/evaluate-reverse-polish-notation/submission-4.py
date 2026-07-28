class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oper = {"+", "-", "*", "/"}
        stack = []

        for num in tokens:
            print(stack)
            if num not in oper:
                stack.append(num)
                continue

            if num == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif num == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif num == "-":
                front = int(stack.pop())
                stack.append(int(stack.pop()) - front)
            elif num == "/":
                front = int(stack.pop())
                stack.append(int(int(stack.pop()) / front))

        return int(stack[0])


    