class Solution:
    # O(log(N)) time
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversedNum = 0
        num = x
        while num > 0:
            reversedNum = (reversedNum * 10) + (num % 10 )
            num = num // 10

        return x == reversedNum

    def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False

        num = str(x)
        l, r = 0, len(num) - 1

        while l < r:
            if num[l] != num[r]:
                return False

            l += 1
            r -= 1
        
        return True