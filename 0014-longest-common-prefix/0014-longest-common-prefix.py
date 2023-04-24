class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans, v = "", sorted(v)
        first, last= v[0], v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans = ''.join([ans, first[i]])
        return ans