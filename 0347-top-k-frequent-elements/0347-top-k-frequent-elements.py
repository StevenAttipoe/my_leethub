class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            buckets[freq].append(num)
            
        topK = []
        for freq in range(len(buckets)-1, -1, -1):
            for num in buckets[freq]:
                topK.append(num)
                if len(topK) == k:
                    return topK