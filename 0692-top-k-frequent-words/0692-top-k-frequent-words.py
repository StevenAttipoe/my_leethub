class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordFreq = {}

        for w in words:
            wordFreq[w] = wordFreq.get(w, 0) + 1
        
        sortedWordFreq = sorted(wordFreq.keys(), key = lambda w: (-wordFreq[w], w))
        
        return sortedWordFreq[:k]


        
        