class Solution:
    def decodeString(self, string: str) -> str:
        n = 0
        substr = []
        stack = []

        for c in string:
            if c == "[":
                stack.append("".join(substr))
                stack.append(n)
                substr.clear()
                n = 0

            elif c == "]":
                v, p = stack.pop(), stack.pop()
                substr = [p + (v * "".join(substr))]

            elif c.isalpha():
                substr.append(c)

            else:
                n = n * 10 + int(c)
        
        return "".join(substr)





            