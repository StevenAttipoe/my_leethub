class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversedWords = words[::-1]
        
        return ' '.join(reversedWords)

        