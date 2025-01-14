class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0

        for num in nums:
            if gas < 0:
                return False
            elif gas < num:
                gas = num
            gas -= 1
        
        return True
        