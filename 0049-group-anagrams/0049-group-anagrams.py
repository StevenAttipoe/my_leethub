class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]

        groups = {}

        for word in strs:
            sortedWord = str(sorted(word))

            if sortedWord in groups:
                groups[sortedWord].append(word)
            else:
                groups[sortedWord] = [word]

        res = []
        for _, values in groups.items():
            subGroup = []
            for word in values:
                subGroup.append(word)
            res.append(subGroup)

        return res