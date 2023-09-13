class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for c1, c2 in zip(s, t):
            if (c1 not in s_map) and (c2 not in t_map):
                s_map[c1] = c2
                t_map[c2] = c1

            elif c1 != t_map.get(c2, 0) or c2 != s_map.get(c1, 0):
                return False
        return True