class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majorityNum = 0

        for n in nums:
            if count == 0:
                majorityNum = n

            if n == majorityNum:
                count += 1
            else:
                count -= 1
        return majorityNum

    def majorityElement2(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxCount = 0
        majorityNum = nums[0]

        for k, v in count.items():
            if maxCount < v:
                majorityNum = k
                maxCount = v

        return majorityNum

        