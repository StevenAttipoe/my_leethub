class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board
        self.path = set()

        for i in range(self.ROWS):
            for j in range(self.COLS):
                if board[i][j] == word[0]:
                    isFound = self.dfs(i, j, word, 0)

                    if isFound:
                        return True

        return False

    def dfs(self, i, j, word, pos):
        if pos == len(word):
            return True

        if i < 0 or i >= self.ROWS or j < 0 or j >= self.COLS:
            return False

        if (i, j) in self.path or self.board[i][j] != word[pos]:
            return False

        self.path.add((i, j))

        result = (self.dfs(i, j + 1, word, pos + 1) or
        self.dfs(i, j - 1, word, pos + 1) or
        self.dfs(i + 1, j, word, pos + 1) or 
        self.dfs(i - 1, j, word, pos + 1))

        self.path.remove((i,j))

        return result

        

        
        