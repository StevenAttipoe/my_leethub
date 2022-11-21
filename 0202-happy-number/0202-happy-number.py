class Solution:
    def isHappy(self, n: int) -> bool:
        nums = []
        _sum = 0
        seen = set()

        while _sum != 1:
            while n != 0:
                nums.append(n % 10)
                n = n // 10

            for i in range(len(nums)):
                nums[i] = nums[i]**2

            _sum = sum(nums)
            if _sum in seen:
                return False
            n = _sum
            nums  = []
            seen.add(_sum)
        return True
            
            