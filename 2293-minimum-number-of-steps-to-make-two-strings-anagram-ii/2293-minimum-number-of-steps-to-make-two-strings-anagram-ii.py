class Solution:
    def minSteps(self, s: str, t: str) -> int:
        charFreqOfS = Counter(s)
        charFreqOfT = Counter(t)

        steps = 0
        for char in set(s + t):
            if charFreqOfT[char] != charFreqOfS[char]:
                steps += abs(charFreqOfT[char] - charFreqOfS[char])

        return steps


        