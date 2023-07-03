class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        T = [False] * len(s)
        for i in range(len(s)):
            for word in wordSet:
                left = i - len(word) + 1
                if left < -1:
                    continue
                if s[left:i+1] in wordSet and (left == 0 or T[left - 1]):
                    T[i] = True
                    break
        return T[len(s) - 1]
            
        

        
        