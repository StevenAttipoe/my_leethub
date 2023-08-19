class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                withoutLeft = s[:l] + s[l + 1:]
                withoutRight = s[:r] + s[r + 1:] 
                return withoutLeft == withoutLeft[::-1] or withoutRight == withoutRight[::-1]

            l += 1
            r -= 1

        return True