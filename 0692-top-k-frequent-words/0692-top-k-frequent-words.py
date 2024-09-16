class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for c in word:
            root = root.children[c]
        root.isEnd = True

    def getAllWords(self, root=None, prefix=[]):
        if not root:
            root = self.root

        words = []

        if root.isEnd:
            words.append("".join(prefix))

        for i in range(26):
            c = chr(i + ord("a"))
            if c in root.children:
                prefix.append(c)
                words += self.getAllWords(root.children[c], prefix)
                prefix.pop()

        return words


class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, p):
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)


class Solution:
    """
    O(N * L) + O(L * K) time

    Given L <= 10, 
    => O(N * 10) + O(10 * K) time
    => O(N) + O(K) time
    => O(N + K) time

    Given K <= N,
    => O(N + K) time
    => O(N + N) time
    => O(N) time

    O(N) space
    """
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordFreq = {}

        for w in words:
            wordFreq[w] = wordFreq.get(w, 0) + 1

        buckets = [Trie() for _ in range(len(words))]

        #O(N * L)
        for w, f in wordFreq.items():
            buckets[f - 1].insert(w)

        result = []

        # O(L * K)
        for i in range(len(buckets) - 1, -1, -1):
            words = buckets[i].getAllWords()
            for w in words:
                if k > 0:
                    result.append(w)
                    k -= 1
                else:
                    return result
        return result

    # O(nlogk) time and O(n) space
    def topKFrequent2(self, words: List[str], k: int) -> List[str]:
        wordFreq = {}

        for w in words:
            wordFreq[w] = wordFreq.get(w, 0) + 1

        heap = []
        for w, f in wordFreq.items():
            heapq.heappush(heap, Pair(w, f))

            if len(heap) > k:
                heapq.heappop(heap)

        return [p.word for p in sorted(heap, reverse=True)]

    # O(n + klogn) time and O(n) space
    def topKFrequent3(self, words: List[str], k: int) -> List[str]:
        wordFreq = {}

        for w in words:
            wordFreq[w] = wordFreq.get(w, 0) + 1

        heap = [(-f, w) for w, f in wordFreq.items()]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]

    # O(nlogn) time and O(n) space
    def topKFrequent4(self, words: List[str], k: int) -> List[str]:
        wordFreq = {}

        for w in words:
            wordFreq[w] = wordFreq.get(w, 0) + 1

        result = sorted(wordFreq.keys(), key=lambda w: (-wordFreq[w], w))
        return result[:k]
