class Solution:
    #O(logr + log(c))
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        
        midRow = 0
        top, bot = 0, ROW - 1
        
        while top <= bot:
            midRow = (top + bot) // 2
            
            if target > matrix[midRow][-1]:
                top = midRow + 1
                
            elif target < matrix[midRow][0]:
                bot = midRow - 1
                
            else:
                break
                
        #Find if target is not in any of the rows
        if not top <= bot:
            return False
        
        left, right = 0, COL - 1    
        while left <= right:
            mid = (left + right) // 2
            
            if target < matrix[midRow][mid]:
                right = mid - 1 
                
            elif target > matrix[midRow][mid]:
                left = mid + 1
            
            else:
                return True
            
        return False
        