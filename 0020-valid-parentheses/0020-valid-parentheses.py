class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pmap = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        for p in s:
            if p in ["(", "{", "["]:
                stack.append(p)
            
            elif stack:
                if stack[-1] != pmap[p]:
                    return False
                else:
                    stack.pop()
            
            else:
                return False

        return True if len(stack) == 0 else False