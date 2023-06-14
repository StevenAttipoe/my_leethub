class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score, maxScore = 0, 0
        i , j = 0, len(tokens) - 1

        while i <= j:
            if power >= tokens[i]:
                power -= tokens[i]
                score += 1
                maxScore = max(score, maxScore)
                i += 1

            elif score > 0:
                score -= 1
                power += tokens[j]
                j -= 1

            else:
                return  maxScore

        return maxScore
