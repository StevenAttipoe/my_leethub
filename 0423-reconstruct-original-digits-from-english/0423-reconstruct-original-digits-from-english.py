class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)
        nums_map = {}

        nums_map[0] = count.get('z', 0)
        nums_map[2] = count.get('w', 0)
        nums_map[4] = count.get('u', 0)
        nums_map[6] = count.get('x', 0)
        nums_map[8] = count.get('g', 0)
        nums_map[1] = count.get('o', 0) - nums_map[0] - nums_map[2] - nums_map[4]
        nums_map[3] = count.get('t', 0) - nums_map[2] - nums_map[8]
        nums_map[5] = count.get('f', 0) - nums_map[4]
        nums_map[7] = count.get('s', 0) - nums_map[6]
        nums_map[9] = count.get('i', 0) - nums_map[5] - nums_map[6] - nums_map[8]

        digits = []
        for digit, freq in nums_map.items():
            digits.append(str(digit) * freq)

        return ''.join(sorted(digits))

    def originalDigits2(self, s: str) -> str:
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




        





        