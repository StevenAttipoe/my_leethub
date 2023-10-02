class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)

            else:
                substring = []
                while stack and stack[-1] != '[':
                    c = stack.pop()
                    substring.append(c)
                stack.pop()

                f = ''
                while stack and stack[-1].isdigit():
                    f = stack.pop() + f


                stack.append(int(f) * ''.join(substring[::-1]))
            
        return ''.join(stack)




        