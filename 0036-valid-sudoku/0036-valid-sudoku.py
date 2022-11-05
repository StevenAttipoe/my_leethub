class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        col = set()
        matrix = set()
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                    
                if ((r,board[r][c]) in row or 
                    (c,board[r][c]) in col or
                    ((r//3,c//3), board[r][c])  in matrix):
                    return False
                
                row.add((r, board[r][c]))
                col.add((c, board[r][c]))
                matrix.add( ((r//3, c//3), board[r][c]) )
        return True