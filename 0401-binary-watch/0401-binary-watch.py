class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        leds = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]

        def backtrack(i, hrs, mins, n):
            if hrs >= 12 or mins >= 60:
                return

            if n == 0:
                time = str(hrs) + ':' + '0'*(mins < 10) + str(mins)
                res.append(time)
                return

            if i < len(leds):
                if i <= 3:
                    backtrack(i + 1, hrs + leds[i], mins, n - 1)
                else:
                    backtrack(i + 1, hrs, mins + leds[i], n - 1)
                backtrack(i+1, hrs, mins, n)

        res = []
        backtrack(0, 0, 0, turnedOn)
        return res






    