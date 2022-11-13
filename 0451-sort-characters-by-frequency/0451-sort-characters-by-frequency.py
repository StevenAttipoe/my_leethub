class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        chars = list(s)
        chars.sort(key = lambda x:(-count[x],x))
        return "".join(chars)
        