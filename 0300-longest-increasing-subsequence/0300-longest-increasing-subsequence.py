class Solution:
    # O(n * log n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = []

        for n in nums:
            i = bisect_left(LIS, n)

            if i == len(LIS):
                LIS.append(n)
            else:
                LIS[i] = n
        return len(LIS)

    #O(n ^ 2) time
    def lengthOfLIS2(self, nums: List[int]) -> int:
        LIS = [nums[0]]

        for n in nums[1:]:
            if n > LIS[-1]:
                LIS.append(n)
            else:
                i = 0
                while LIS[i] < n: 
                    i += 1
                LIS[i] = n
            print(LIS)
        return len(LIS)


    #O(n ^ 2) time
    def lengthOfLIS2(self, nums: List[int]) -> int:
        LEN = len(nums)
        LIS = [1] * LEN

        for i in range(LEN - 1, -1, -1):
            for j in range(i, LEN):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)
        