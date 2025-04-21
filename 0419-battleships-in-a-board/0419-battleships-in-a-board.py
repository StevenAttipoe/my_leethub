class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        COLS = len(board)
        ROWS = len(board[0])
        count = 0

        for i in range(COLS):
            for j in range(ROWS):
                if board[i][j] == 'X':
                    self.dfs(i, j, board)
                    count += 1
        return count

    
    def dfs(self, i, j, board):
        COLS = len(board)
        ROWS = len(board[0])

        if i >= COLS or i < 0 or j >= ROWS or j < 0 or board[i][j] == '.':
            return
        
        board[i][j] = '.'
        self.dfs(i + 1, j, board)
        self.dfs(i - 1, j, board)
        self.dfs(i, j + 1, board)
        self.dfs(i, j - 1, board)



        