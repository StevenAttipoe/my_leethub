class Solution:
    def romanToInt(self, s: str) -> int:
        SYMBOLS = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        num = i = 0
        while i < len(s) - 1:
            if SYMBOLS[s[i]] < SYMBOLS[s[i + 1]]:
                num += SYMBOLS[s[i + 1]] - SYMBOLS[s[i]]
                i += 2
            else:
                num += SYMBOLS[s[i]]
                i += 1

        if i < len(s):
            num += SYMBOLS[s[i]]

        return num


        