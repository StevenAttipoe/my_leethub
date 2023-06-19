class Solution:
    def minSteps(self, s: str, t: str) -> int:
        charFreq = Counter(s)
        steps = 0

        for char in t:
            if char in charFreq:
                charFreq[char] -= 1

                if not charFreq[char]:
                    del charFreq[char]
            
            else:
                steps += 1

        return steps