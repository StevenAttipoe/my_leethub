class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxScore = 0
        curMax = values[0] - 1

        for i in range(1, len(values)):
            maxScore = max(maxScore, values[i] + curMax)
            curMax = max(curMax - 1, values[i] - 1)

        return maxScore

        