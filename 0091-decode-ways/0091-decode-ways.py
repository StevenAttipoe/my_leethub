class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        one_back = two_back = 1
        for i in range(2, len(s) + 1):
            cur = 0
            if 1 <= int(s[i - 1]) <= 9:
                cur += one_back
            
            if 10 <= int(s[i - 2] + s[i - 1]) <= 26:
                cur += two_back

            two_back = one_back
            one_back = cur

        return one_back

    def numDecodings2(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = dp[1] = 1

        if s[0] == '0':
            return 0
        
        for i in range(2, len(dp)):
            if 1 <= int(s[i - 1]) <= 9:
                dp[i] += dp[i - 1]
            
            if 10 <= int(s[i - 2] + s[i - 1]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]
        