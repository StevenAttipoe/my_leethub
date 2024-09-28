class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            j, k = i + 1, n - 1  
            while j < k:
                a, b, c = nums[i], nums[j], nums[k]
                totalSum = a + b + c

                if totalSum == 0:
                    result.append([a,b,c])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                elif totalSum > 0:
                    k -= 1
                else:
                    j += 1
        
        return result

    # O(N^3) time
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if i != j or j != k or i != k:
                        if nums[i] + nums[j] + nums[k] == 0:
                            result.add((nums[i], nums[j], nums[k]))

        return result
        
        