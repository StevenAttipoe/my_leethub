class Solution:
    def calculate(self, s: str) -> int:
        operands = ['-', '+', '*', '/']
        stack = []
        digit, sign = 0, "+" 

        for char in s + '+':
            if char.isdigit():
                digit = digit * 10 + int(char)

            elif char in operands:
                match sign:
                    case '+':
                        stack.append(digit)
                    case '-':
                        stack.append(-digit)
                    case '/':
                        if stack: stack.append(int(stack.pop() / digit))
                    case '*':
                        if stack: stack.append(stack.pop() * digit)
                digit = 0
                sign = char
        return sum(stack)