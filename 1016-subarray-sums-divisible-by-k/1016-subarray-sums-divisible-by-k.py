class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counts = [0 for i in range(k)]
        runningSum = 0
        
        for num in nums:
            runningSum += num
            remainder = runningSum % k
            counts[remainder] += 1

        # Fine no of ways to get a subarray divisible by k
        # If two remainders are the same, it means that the ranges in between are div by k
        # nCr => n (n - 1) // 2
        result = counts[0]
        for c in counts:
            result += (c * (c - 1)) // 2 
        return result


    def subarraysDivByK2(self, nums: List[int], k: int) -> int:
        res = 0
        runningSum = 0
        sums = {0 : 1}

        for num in nums:
            runningSum += num
            r = runningSum % k

            if r in sums:
                res += sums[r]
                sums[r] += 1
                continue

            sums[r] = 1
        
        return res


