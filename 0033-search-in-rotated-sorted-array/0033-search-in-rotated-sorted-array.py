class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = 0
        # start, end = 0, len(nums)
        # while start <= end:
        #     mid = start + (start - end) // 2
        #     if nums[mid - 1] > nums[mid]:
        #         pivot = mid
        #     else:
        #         left = mid + 1

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                pivot = i
                break

        print(pivot)
        start = end = 0
        if nums[pivot] <= target <= nums[-1]:
            start, end = pivot, len(nums)
        else:
            start, end = 0, pivot - 1

        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1



        
        