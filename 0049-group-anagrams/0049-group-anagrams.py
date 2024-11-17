class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)

        for s in strs:
            anagramMap["".join(sorted(s))].append(s)
        
        return list(anagramMap.values())
        