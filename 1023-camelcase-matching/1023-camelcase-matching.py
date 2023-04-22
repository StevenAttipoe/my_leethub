class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def match(pattern, query):
            i = 0
            for j, char in enumerate(query):
                if i < len(pattern) and pattern[i] == query[j]: 
                    i += 1
                elif query[j].isupper(): 
                    return False
            return i == len(pattern)
        
        return [match(pattern, query) for query in queries]