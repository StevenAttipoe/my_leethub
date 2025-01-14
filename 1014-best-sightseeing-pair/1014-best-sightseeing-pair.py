class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxScore = 0
        curMax = values[0] - 1

        for i in range(1, len(values)):
            maxScore = max(maxScore, values[i] + curMax)
            curMax = max(curMax - 1, values[i] - 1)

        return maxScore

    def maxScoreSightseeingPair2(self, values: List[int]) -> int:
        maxScore = -math.inf

        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                score = values[i] + values[j] + (i - j)
                maxScore = max(maxScore, score)
        
        return maxScore

        