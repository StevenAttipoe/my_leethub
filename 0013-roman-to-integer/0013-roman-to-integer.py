class Solution:
    def romanToInt(self, s: str) -> int:
        val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        digit = 0

        for i, char in enumerate(s):
            if i < len(s) - 1 and val[char] < val[s[i + 1]]:
                digit -= val[char]
            else:
                digit += val[char]

        return digit


        