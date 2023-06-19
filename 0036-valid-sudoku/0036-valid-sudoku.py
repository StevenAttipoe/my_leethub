class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        elements = []
        
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    digit = board[r][c]
                    elements += [(r, digit), (digit, c), (r//3, c//3, digit)]
        return len(elements) == len(set(elements))

