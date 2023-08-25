class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        buckets = [[] for i in range(len(nums) + 1)]

        for key, value in freq.items():
            buckets[value].append(key)

        topK = []
        for i in range(len(buckets) - 1, -1, -1):
            for element in buckets[i]:
                topK.append(element)

                if len(topK) == k:
                    return topK
