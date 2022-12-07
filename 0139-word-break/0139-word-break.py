class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        
        def wordBreakHelper(word, l, memo):
            if l == len(word):
                return True
            
            if l in memo:
                return memo[l]
            
            for r in range(l + 1, len(word) + 1):
                prefix = word[l:r]
                if prefix in wordSet and wordBreakHelper(word, r, memo):
                    memo[r] = True
                    return True
                memo[l] = False
            return False
        return wordBreakHelper(s, 0, {})
                    
        
        