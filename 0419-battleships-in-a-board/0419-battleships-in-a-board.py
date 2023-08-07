class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    count += 1
                    self.dfs(board, i, j)
        return count

    def dfs(self, board, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] == '.':
            return

        board[i][j] = '.'

        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j + 1)
        self.dfs(board, i, j - 1)


        