class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oper = {"+", "-", "*", "/"}
        stack = []

        for num in tokens:
            print(stack)
            if num not in oper:
                stack.append(int(num))
                continue

            if num == "+":
                stack.append(stack.pop() + stack.pop())
            elif num == "*":
                stack.append(stack.pop() * stack.pop())
            elif num == "-":
                front = stack.pop()
                stack.append(stack.pop() - front)
            elif num == "/":
                front = stack.pop()
                stack.append(int(stack.pop() / front))

        return stack[0]


    