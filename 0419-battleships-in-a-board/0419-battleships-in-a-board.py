class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        COLS = len(board)
        ROWS = len(board[0])
        count = 0


        def dfs(i, j):
            if i >= COLS or i < 0 or j >= ROWS or j < 0 or board[i][j] == '.':
                return
            
            board[i][j] = '.'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(COLS):
            for j in range(ROWS):
                if board[i][j] == 'X':
                    dfs(i, j)
                    count += 1
        return count

    




        