class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []

        def backtrack(start, comb):
            if k == len(comb):
                combinations.append(comb[:])
                return

            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()

        backtrack(1, [])
        return combinations
        