class Solution:
    def reorganizeString(self, s: str) -> str:
        charTable = {}
        N = len(s)

        for c in s:
            charTable[c] = charTable.get(c, 0) + 1

        sortedChars = sorted(charTable, key = lambda c: charTable[c], reverse = True)

        if charTable[sortedChars[0]] > (N + 1) // 2:
            return ""

        result = [''] * N
        i = 0

        for c in sortedChars:
            for _ in range(charTable[c]):
                if i >= N:
                    i = 1

                result[i] = c
                i += 2

        return ''.join(result)