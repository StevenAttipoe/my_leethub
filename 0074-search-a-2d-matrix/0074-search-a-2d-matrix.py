class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        targetRow = None
        for r in range(ROWS):
            s, e = matrix[r][0], matrix[r][COLS - 1]

            if s <= target <= e:
                print(r)
                targetRow = r
                break 
        
        if targetRow is None:
            return False
        
        l, r = 0, COLS - 1
        while l <= r:
            mid = (r + l) // 2
            
            if matrix[targetRow][mid] == target:
                return True
            
            elif matrix[targetRow][mid] < target:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return False
            
            
        