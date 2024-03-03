class Solution:
    """ 
    O(N * 3^L) time
    N - The number of cells in the board
    L - length of the word

    O(L) space
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    isFound = self.dfs(i, j, board, word)
                    if isFound:
                        return True

        return False

    def dfs(self, i, j, board, suffix):
        if len(suffix) == 0:
            return True

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) \
                or board[i][j] != suffix[0]:
            return False

        temp = board[i][j]
        board[i][j] = '#'

        isFound = (
            self.dfs(i + 1, j, board, suffix[1:]) or
            self.dfs(i - 1, j, board, suffix[1:]) or
            self.dfs(i, j + 1, board, suffix[1:]) or
            self.dfs(i, j - 1, board, suffix[1:])
        )

        board[i][j] = temp
        return isFound
