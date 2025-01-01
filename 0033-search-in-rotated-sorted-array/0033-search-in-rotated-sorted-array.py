class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        l, r = 0, n - 1
        while l <= r:
            mid = (r + l) // 2

            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid - 1
        
        def bs(l, r):
            while l <= r:
                mid = (r + l) // 2
                
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        if nums[-1] < target:
            return bs(0, l)
        return bs(l, n - 1)

            
        