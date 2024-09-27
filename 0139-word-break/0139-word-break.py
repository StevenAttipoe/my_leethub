class Solution:
    def wordBreak(self, s: str, wordList: List[str]) -> bool:
        wordSet = set(wordList)

        @cache
        def recurse(p):
            if p == len(s):
                return True

            for word in wordSet:
                for i in range(p, len(s)):
                    substr = s[p: i + 1]
                    if word == substr:
                        if recurse(i + 1):
                            return True
            return False

        return recurse(0)
