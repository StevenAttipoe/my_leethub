class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = 0
        start, end = 0, len(nums) - 1

        #Find pivot
        while start <= end:
            mid = (end + start) // 2
            if nums[mid] > nums[-1]:
                start = mid + 1
            else:
                end = mid - 1

        pivot = start
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            shifted_mid = (pivot + mid) % len(nums)
            if nums[shifted_mid] == target:
                return shifted_mid
            elif nums[shifted_mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    # # def search2(self, nums: List[int], target: int) -> int:
    #     low = 0
    #     high = len(nums) - 1

    #     while low < high:
    #         mid = (low + high) // 2
    #         if nums[mid] > nums[high]:
    #             low = mid + 1
    #         else:
    #             high = mid 

    #     rotated = low
    #     max_nums = (rotated - 1) % len(nums)

    #     if nums[rotated] <= target <= nums[max_nums]:
    #         low = 0
    #         high = len(nums) - 1
            
    #         while low <= high:
    #             mid = (low + high) // 2
    #             real_mid = (mid + rotated) % len(nums)

    #             if target < nums[real_mid]:
    #                 high = mid - 1
    #             elif target > nums[real_mid]:
    #                 low = mid + 1
    #             else:
    #                 return real_mid
    #     return -1
        