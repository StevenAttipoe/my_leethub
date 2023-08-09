class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        pairs = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                pairs.append(''.join(stack))
                return

            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closeN)
                stack.pop()

            if openN > closeN:
                stack.append(')')
                backtrack(openN, closeN + 1)
                stack.pop()

        backtrack(0, 0)
        return pairs

        