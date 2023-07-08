class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        prev, cur = symbols[s[0]], 0
        integer = 0
        for char in s[1:]:
            cur = symbols[char]
            if prev < cur:
                integer -= prev
            else:
                integer += prev
            prev = cur
        integer += prev

        return integer
        


        