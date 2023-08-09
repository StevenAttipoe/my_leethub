class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col = 0
        
        for i, c in enumerate(reversed(columnTitle)):
            digit = ord(c) - ord('A') + 1
            col += digit * 26 ** i
        return col