class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
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
        