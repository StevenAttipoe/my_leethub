class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        chain = 0
        pairs.sort(key = lambda x:x[1])
        cur = float('-inf')

        for pair in pairs:
            if pair[0] > cur:
                cur = pair[1]
                chain += 1

        return chain