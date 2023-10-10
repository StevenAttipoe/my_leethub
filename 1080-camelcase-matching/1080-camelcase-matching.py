class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []

        for query in queries:
            i = 0
            for char in query:
                if i < len(pattern) and pattern[i] == char:
                    i += 1
                elif char.isupper():
                    res.append(False)
                    break
            else:
                res.append(i == len(pattern))

        return res
        