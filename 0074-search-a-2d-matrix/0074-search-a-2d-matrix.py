class Solution:
    # O(m * log(n)) time
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        targetRow = None
        l, r = 0, ROWS - 1
        while l <= r:
            mid = (r + l) // 2
            s, e = matrix[mid][0], matrix[mid][COLS - 1]

            if s <= target <= e:
                targetRow = mid
                break 
            
            elif target < s:
                r = mid - 1

            elif target > e:
                l = mid + 1
        
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
            
            
        