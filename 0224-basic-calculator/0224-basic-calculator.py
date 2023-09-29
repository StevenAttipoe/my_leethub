class Solution:
    def calculate(self, s: str) -> int:
        ans = digit = 0
        sign = 1
        stack = [sign]

        for char in s:
            if char.isdigit():
                digit = digit * 10 + int(char)
            elif char == '(':
                stack.append(sign)
            elif char == ')':
                stack.pop()
            elif char == "+" or char == "-":
                ans += sign * digit
                sign = (1 if char == '+' else -1) * stack[-1]
                digit = 0
        
        return ans + sign * digit