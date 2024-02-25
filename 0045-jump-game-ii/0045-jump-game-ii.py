class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums) - 1
        minJumps = 0
        jumpEnd = farthestStep = 0

        for i in range(N):
            farthestStep = max(farthestStep, i + nums[i])

            if farthestStep >= N:
                minJumps += 1
                return minJumps
            
            if i == jumpEnd:
                jumpEnd = farthestStep
                minJumps += 1

        return minJumps
            

    def jump2(self, nums: List[int]) -> int:
        minJumps = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            l = r + 1
            r = farthest
            minJumps += 1

        return minJumps
        