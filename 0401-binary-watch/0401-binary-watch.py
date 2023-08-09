class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        time = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
        res = []

        def backtrack(n, start, h, m):
            if n == 0 and h < 12 and m < 60:
                res.append(f"{h}:{m:02}")
                return

            for i in range(start, len(time)):
                if i < 4:
                    h += time[i]
                    n -= 1
                    backtrack(n, i + 1, h, m)
                    n += 1
                    h -= time[i]
                else:
                    m += time[i]
                    n -=  1
                    backtrack(n, i + 1, h, m)
                    n += 1
                    m -= time[i]

        backtrack(turnedOn, 0, 0, 0)
        return res





    