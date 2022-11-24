class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                
                if stack[-1][1] == 2:
                    stack.pop()
            else:
                stack.append([c, 1])
            
        return "".join(c * count for c, count in stack)