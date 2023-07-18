class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = 0
        min_diff = inf

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                nums_sum = nums[i] + nums[j] + nums[k]
                diff = abs(target - nums_sum)
                if diff < min_diff:
                    min_diff = diff
                    closest_sum = nums_sum

                if nums_sum < target:
                    j += 1
                elif nums_sum > target:
                    k -= 1
                else:
                    return closest_sum

        return closest_sum



        