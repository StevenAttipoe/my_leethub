class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = {}
        l, ans = 0, 0

        for r, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1
            
            while counts[char] > 1:
                counts[s[l]] -= 1
                l += 1
            
            ans = max(ans, (r - l + 1))

        return ans



        