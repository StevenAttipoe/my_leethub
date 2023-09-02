class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
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