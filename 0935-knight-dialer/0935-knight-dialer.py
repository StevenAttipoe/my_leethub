class Solution:
    def knightDialer(self, n: int) -> int:
        DIALS = {
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

        counts = [1] * 10
        for _ in range(n-1):
            curCount = [0] * 10
            for src in range(10):
                for des in DIALS[src]:
                    curCount[des] +=  counts[src] % (10 ** 9 + 7)
            counts = curCount

        return sum(counts) % (10 ** 9 + 7)