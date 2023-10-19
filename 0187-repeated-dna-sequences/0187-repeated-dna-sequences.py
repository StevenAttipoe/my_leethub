class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dna_map = {}
        res = []

        for i in range(len(s) - 9):
            dna = s[i:i + 10]
            dna_map[dna] = dna_map.get(dna, 0) + 1
            if dna_map[dna] == 2:
                res.append(dna)

        return res


    def findRepeatedDnaSequences2(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        seen = set()
        res = set()

        for i in range(len(s) - 9):
            seq = s[i:i + 10]
            if seq in seen:
                res.add(seq)
            else:
                seen.add(seq)

        return res
        