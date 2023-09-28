class Solution:
    #O(n) time & space
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        # -1 for elements still in stack for n interations
        for height in heights + [-1]:
            maxWidth = 0

            while stack and stack[-1][1] >= height: #while cannot extend
                w, h = stack.pop()
                maxWidth += w
                maxArea = max(maxArea, maxWidth * h)
            
            stack.append((maxWidth + 1, height))

        return maxArea


        
        