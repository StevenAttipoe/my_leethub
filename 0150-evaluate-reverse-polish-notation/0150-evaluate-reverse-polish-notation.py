import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {
            '*': operator.mul,
            '+': operator.add,
            '-': operator.sub,
            '/': operator.truediv
        }

        for char in tokens:
            if char in operands:
                num2, num1 = stack.pop(), stack.pop()
                ans = operands[char](num1, num2)
                stack.append(int(ans))
            else:
                stack.append(int(char))

        return stack.pop()


        