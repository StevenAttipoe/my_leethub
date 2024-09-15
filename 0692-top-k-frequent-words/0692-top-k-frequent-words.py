class Solution:
    # O(n + klogn) time and O(n) space
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordFreq = {}

        for w in words:
            wordFreq[w] = wordFreq.get(w, 0) + 1

        heap = [(-f, w) for w,f in wordFreq.items()]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]

    # O(nlogn) time and O(n) space
    def topKFrequent2(self, words: List[str], k: int) -> List[str]:
        wordFreq = {}

        for w in words:
            wordFreq[w] = wordFreq.get(w, 0) + 1

        result = sorted(wordFreq.keys(), key = lambda w: (-wordFreq[w], w))
        return result[:k]

    def topKFrequent2(self, words: List[str], k: int) -> List[str]:
        words.sort()
        wordFreq = {}

        for w in words:
            wordFreq[w] = wordFreq.get(w, 0) + 1

        buckets = [[] for i in range(len(words))]

        for w,f in wordFreq.items():
            buckets[f - 1].append(w)

        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for w in buckets[i]:
                if k > 0:
                    result.append(w)
                    k -= 1
                else:
                    return result
        return result
        