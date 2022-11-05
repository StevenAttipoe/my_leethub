class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        visitedCol = defaultdict(set)
        visitedRow = defaultdict(set)
        visitedMatrix = defaultdict(set)
        
        for col in range(9):
            for row in range(9):
                if board[col][row] == ".":
                    continue
                    
                if (board[col][row] in visitedCol[col] or
                   board[col][row] in visitedRow[row] or
                   board[col][row] in visitedMatrix[(col//3,row//3)]):
                    return False
                
                visitedCol[col].add(board[col][row])
                visitedRow[row].add(board[col][row])
                visitedMatrix[(col//3, row//3)].add(board[col][row])
                
        return True
        