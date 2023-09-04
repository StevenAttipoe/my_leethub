class Solution:
    #Counting sort: O(n + k) runtime
    def sortArray2(self, nums: List[int]) -> List[int]:
        minVal, maxVal = min(nums), max(nums)
        counts = {}
        index = 0

        for val in nums:
            counts[val] = counts.get(val, 0) + 1

        for k in range(minVal, maxVal + 1, 1):
            while counts.get(k, 0) > 0:
                nums[index] = k
                counts[k] -= 1
                index += 1

        return nums

    #Merge sort: O(nlogn) runtime
    def sortArray(self, nums: List[int]) -> List[int]:
        temp = [0] * len(nums)

        def merge(left, mid, right):
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if temp[i] < temp[j]:
                    nums[left] = temp[i]
                    left += 1
                    i += 1
                else:
                    nums[left] = temp[j]
                    left += 1
                    j += 1

            while i <= mid:
                nums[left] = temp[i]
                left += 1
                i += 1 

            while j <= right:
                nums[left] = temp[j]
                left += 1
                j += 1

        def divide(low, high):
            if low >= high:
                return
            mid = (low + high) // 2
            divide(low, mid)
            divide(mid + 1, high)

            # Copy the elements to temp before merging
            for i in range(low, high + 1):
                temp[i] = nums[i]

            merge(low, mid, high)

        divide(0, len(nums) - 1)
        return nums



        