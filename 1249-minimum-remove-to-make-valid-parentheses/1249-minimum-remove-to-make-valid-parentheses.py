class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        strArr = list(s)
        stack = []

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    strArr[i] = ''
        
        while stack:
            i = stack.pop()
            strArr[i] = ''

        return "".join(strArr)


        