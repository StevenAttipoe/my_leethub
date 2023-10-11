class Solution:
    def originalDigits(self, s: str) -> str:
        nums_map = {
            'w': ('two', '2'),
            'u': ('four', '4'),
            'x': ('six', '6'),
            'g': ('eight', '8'),
            'z': ('zero', '0'),
            'f': ('five', '5'),
            'r': ('three', '3'), 
            's': ('seven', '7'),
            'i': ('nine', '9'),
            'n': ('one', '1')
        }

        digits = []
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1

        for id, (word, digit) in nums_map.items():
            freq = count.get(id, 0)
            digits.append(digit * freq)

            for char in word:
                if char in count:
                    count[char] -= freq

        return ''.join(sorted(digits))




        





        