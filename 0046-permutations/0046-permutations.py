class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def helper(permutation):
            if len(permutation) == len(nums):
                permutations.append(permutation[:])
                return

            for num in nums:
                if num not in permutation:
                    permutation.append(num)
                    helper(permutation)
                    permutation.pop() #recursively pop (x2)

        helper([])
        
        return permutations


    def permute2(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def helper(i):
            if i == len(nums):
                permutations.append(nums[:])
                return

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                helper(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        helper(0)
        
        return permutations

    def permute3(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = Counter(nums)

        def helper(cur):
            if len(cur) == len(nums):
                res.append(cur)
                return

            for num in count.keys():
                if count[num]:
                    count[num] -= 1
                    helper(cur + [num])
                    count[num] += 1

        helper([])
        return res

        

        