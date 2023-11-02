class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxWindow = []
        q = deque()
        l = r = 0

        while r < len(nums):
            # pop values less than current value
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            # remove left val from window to maintain size
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                maxWindow.append(nums[q[0]])
                l += 1
            r += 1

        return maxWindow

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        maxWindow = []

        for i in range(len(nums) - k + 1):
            high = max(nums[i:i + k])
            maxWindow.append(high)

        return maxWindow