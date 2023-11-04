class Solution:
    def superEggDrop(self, eggs: int, floors: int) -> int: # O(e * f) time & O(e * f) space
        dp = [[0] * (floors + 1) for _ in range(eggs + 1)]

        for i in range(floors + 1):
            dp[1][i] = i

        for e in range(2, eggs + 1):
            k = 1
            for f in range(1, floors + 1):
                while k <= f and dp[e][f - k] > dp[e - 1][k - 1]:
                    k += 1
                dp[e][f] = 1 + dp[e -  1][k - 1]

        return dp[-1][-1]

    def superEggDrop2(self, eggs: int, floors: int) -> int: # O(e * f * k) time & O(e * f) space
        dp = [[0] * (floors + 1) for _ in range(eggs + 1)]

        for i in range(floors + 1):
            dp[1][i] = i

        for e in range(2, eggs + 1):
            for f in range(1, floors + 1):
                dp[e][f] = math.inf
                for k in range(1, f + 1):
                    moves = 1 + max(dp[e - 1][k - 1], dp[e][f - k])
                    dp[e][f] = min(dp[e][f], moves)

        return dp[-1][-1]
