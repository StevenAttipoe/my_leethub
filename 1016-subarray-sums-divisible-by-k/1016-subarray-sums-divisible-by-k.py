class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counts = [0 for i in range(k)]
        runningSum = 0
        
        for num in nums:
            runningSum += num
            remainder = runningSum % k
            counts[remainder] += 1

        result = counts[0]
        for c in counts:
            result += (c * (c - 1)) // 2
        return result






# class Solution:
#     def subarraysDivByK(self, A: List[int], K: int) -> int:
#         prefix_sum = 0
#         sums = {0: 1}
#         answer = 0
#         for num in A:
#             prefix_sum += num
#             key = prefix_sum%K
#             if key in sums:
#                 answer += sums[key]
#                 sums[key] += 1
#                 continue
#             sums[key] = 1
#         return answer

