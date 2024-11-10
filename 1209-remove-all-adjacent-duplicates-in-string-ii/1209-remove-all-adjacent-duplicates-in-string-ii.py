class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [["#", -1]]

        for char in s:
            if stack[-1][0] == char:
                stack[-1][1] += 1

                if stack[-1][1] == k:
                    stack.pop()
            
            else:
                stack.append([char, 1])
        
        return "".join([char * freq for char, freq in stack])
        

    # O(N + k) time
    def removeDuplicates2(self, s: str, k: int) -> str:
        stack = []

        for char in s:
            if stack:
                if len(stack) >= k and len(set(stack[-k:])) == 1:
                    for _ in range(k): stack.pop()
            stack.append(char)

        if len(stack) >= k and len(set(stack[-k:])) == 1:
            for _ in range(k): stack.pop()
            

        return "".join(stack)

        