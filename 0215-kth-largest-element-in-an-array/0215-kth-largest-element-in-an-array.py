class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minVal, maxVal = min(nums), max(nums)
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for num in range(maxVal, minVal - 1, -1):
            while counts.get(num, 0) > 0:
                counts[num] -= 1
                k -= 1

                if not k:
                    return num


    def findKthLargest2(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]