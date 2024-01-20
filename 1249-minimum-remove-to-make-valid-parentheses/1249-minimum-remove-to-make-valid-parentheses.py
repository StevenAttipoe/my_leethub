class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        chars = list(s)

        for i in range(len(s)):
            if chars[i] == '(':
                stack.append(i)
            elif chars[i] == ')':
                if stack:
                    stack.pop()
                else:
                    chars[i] = ''

        for i in stack:
            chars[i] = ''

        return ''.join(chars)


                

            

        