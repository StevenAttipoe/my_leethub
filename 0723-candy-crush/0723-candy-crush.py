class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        if not board:
            return board
        
        ROWS, COLS = len(board), len(board[0])
        isDone = True

        for r in range(ROWS):
            for c in range(COLS - 2):
                if abs(board[r][c]) == abs(board[r][c + 1]) == abs(board[r][c + 2]) and board[r][c] != 0:
                    board[r][c] = -abs(board[r][c])
                    board[r][c + 1] = -abs(board[r][c + 1])
                    board[r][c + 2] = -abs(board[r][c + 2])
                    isDone = False
        

        for c in range(COLS):
            for r in range(ROWS - 2):
                if abs(board[r][c]) == abs(board[r + 1][c]) == abs(board[r + 2][c]) and board[r][c] != 0:
                    board[r][c] = -abs(board[r][c])
                    board[r + 1][c] = -abs(board[r + 1][c])
                    board[r + 2][c] = -abs(board[r + 2][c])
                    isDone = False

        if not isDone:
            for c in range(COLS):
                lastRowIndex = len(board) - 1

                for r in range(ROWS - 1, -1, -1):
                    if board[r][c] > 0:
                        board[lastRowIndex][c] = board[r][c]
                        lastRowIndex -= 1
                
                for r in range(lastRowIndex, -1, -1):
                    board[r][c] = 0
        
        return board if isDone else self.candyCrush(board)
        