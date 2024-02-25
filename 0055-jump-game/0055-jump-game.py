class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0

        for n in nums:
            if gas < 0:
                return False

            elif n > gas:
                gas = n
            
            gas -= 1

        return True

    def canJump2(self, nums: List[int]) -> bool:
        lastIndex = len(nums) - 1

        for curIndex in range(len(nums) - 2, -1, -1):
            jumpStep = nums[curIndex]
            if curIndex + jumpStep >= lastIndex:
                lastIndex = curIndex

        return lastIndex == 0

    def canJump3(self, nums: List[int]) -> bool:
        N = len(nums)
        dp = [False] * N
        dp[0] = True

        for i in range(N):
            if dp[i]:
                jumpStep = nums[i]
                for j in range(1, jumpStep + 1):
                    #Set reachable index to True
                    if i + j < N:
                        dp[i + j] = True

                    #If can jump to last index
                    if i + j == N - 1:
                        return True

        return dp[-1]