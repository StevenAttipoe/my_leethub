class Solution:
    def decodeString(self, s: str) -> str:
        substr = []
        stack = []
        digit = 0

        for char in s:
            if char == "[":
                stack.append("".join(substr))
                stack.append(digit)
                substr.clear()
                digit = 0

            elif char == "]":
                freq, prevStr = stack.pop(), stack.pop()
                substr = [prevStr + (freq * "".join(substr)) ]

            elif char.isdigit():
                digit = (digit * 10) + int(char)
            else:
                substr.append(char)
        
        return "".join(substr)

        