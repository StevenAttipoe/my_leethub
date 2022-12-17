class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        preferred = {}
        for x, y in pairs:
            preferred[x] = set(preferences[x][:preferences[x].index(y)])
            preferred[y] = set(preferences[y][:preferences[y].index(x)])
            
        n = 0    
        for x in preferred.keys():
            for y in preferred[x]:
                if x in preferred[y]:
                    n += 1
                    break 
        return n
                    
        