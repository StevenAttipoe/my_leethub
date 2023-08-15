class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quad = set()
        nums.sort()

        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                c = b + 1
                d = len(nums) - 1

                while c < d:
                    total = nums[a] + nums[b] + nums[c] + nums[d]
                    if total > target:
                        d -= 1
                    elif total < target:
                        c += 1
                    else:
                        quad.add(tuple(sorted((nums[a], nums[b], nums[c], nums[d]))))
                        c += 1
                        d -= 1

        return quad
            
