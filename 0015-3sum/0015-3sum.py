class Solution:  
    # O(N^2) time
    # O(N) space
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = set()
        duplicates = set()

        for i in range(n - 2):
            if nums[i] in duplicates:
                continue

            seen = set()
            j = i + 1

            while j < len(nums):
                complement = -(nums[i] + nums[j])

                if complement in seen:
                    result.add(tuple(sorted((nums[i], nums[j], complement))))

                    while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                        j += 1
                
                seen.add(nums[j])
                j += 1
            
            duplicates.add(nums[i])
        
        return result

    # O(N^2) time
    # O(log n or n) time
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []

        def twoSum(i, nums, result):
            n = len(nums)
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

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            twoSum(i, nums, result)
        
        return result

    # O(N^2) time
    # O(N) space
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []

        def twoSum(i, nums, result):
            seen = set()
            j = i + 1

            while j < len(nums):
                complement = -(nums[i] + nums[j])

                if complement in seen:
                    result.append([nums[i], nums[j], complement])

                    while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                        j += 1
                
                seen.add(nums[j])
                j += 1

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            twoSum(i, nums, result)
        
        return result

    # O(N^3) time
    def threeSum3(self, nums: List[int]) -> List[List[int]]:
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

    # O(N^3) time
    def threeSum4(self, nums: List[int]) -> List[List[int]]:
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
        
        