class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        maxScore = -math.inf

        dp = [0] * n
        dp[0] = values[0]

        for i in range(1, n):
            dp[i] = max(dp[i - 1], values[i - 1] + i - 1)
            maxScore = max(maxScore, dp[i] + values[i] - i)
        
        return maxScore



    def maxScoreSightseeingPair2(self, values: List[int]) -> int:
        maxScore = -math.inf

        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                score = values[i] + values[j] + (i - j)
                maxScore = max(maxScore, score)
        
        return maxScore

        