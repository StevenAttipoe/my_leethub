class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: 
            return ""

        res = strs[0]
        for i in range(1, len(strs)):
            cur = strs[i]
            temp = ""
            for j in range(min(len(cur), len(res))):
                if cur[j]==res[j]: 
                    temp += cur[j]
                else: break
            res = temp

        return res
                
