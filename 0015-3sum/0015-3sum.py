class Solution:
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
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
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                for k in range(j + 1, n):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue

                    if i != j or j != k or i != k:
                        if nums[i] + nums[j] + nums[k] == 0:
                            result.append((nums[i], nums[j], nums[k]))

        return result
        
        