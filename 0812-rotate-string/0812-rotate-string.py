class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        pivot = 0
        n = len(s)

        for i in range(n):
            if s[i:] == goal[:n - i]:
                pivot = i
                break

        return s[pivot:] + s[:pivot] == goal

        