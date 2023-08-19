class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = []
        for char in s:
            if char.isalnum():
                phrase.append(char.lower())

        l, r = 0, len(phrase) - 1
        while l <= r:
            if phrase[l] != phrase[r]:
                return False
            l += 1
            r -= 1

        return True
