class Solution:
    def knightDialer(self, n: int) -> int:
        DIALS = {
            -1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            0:[4, 6], 
            1: [6, 8], 
            2: [7, 9], 
            3: [4, 8], 
            4: [0, 3, 9], 
            5: [] ,
            6: [0, 1, 7], 
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
            }

        return self.knightDialerHelper(DIALS, n, -1, {})

    def knightDialerHelper(self, dials, idx, cur, cache):
        if (idx, cur) in cache:
            return cache[(idx, cur)]

        if idx == 0:
            return 1

        count = 0
        for num in dials[cur]:
            count += self.knightDialerHelper(dials, idx - 1, num, cache)

        cache[(idx, cur)] = count
        return count % (10 ** 9 + 7)