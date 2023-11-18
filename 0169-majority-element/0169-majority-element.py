class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxCount = 0
        majorityNum = nums[0]

        for k, v in count.items():
            if maxCount < v:
                majorityNum = k
                maxCount = v

        return majorityNum

        