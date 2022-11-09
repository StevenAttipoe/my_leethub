class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N, M = len(matrix), len(matrix[0])
        
        r, c = N - 1, 0
        while r >= 0 and c < M:
            if matrix[r][c] == target:
                return True
            
            elif target > matrix[r][c]:
                c += 1
                
            else:
                r -= 1
        return False