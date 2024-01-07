class Solution:
    """
    alive -> dies -> n < 2 or n > 3
    alive -> lives -> n == 2 or n == 3
    dead -> lives -> n == 3
    """
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])

        def countLiveNeighbours(r, c):
            count = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if(i < 0 or j < 0 or i >= ROWS or j >= COLS): continue
                    if((i,j) != (r,c) and board[i][j] & 1):
                        count += 1
            return count

        for i in range(ROWS):
            for j in range(COLS):
                count = countLiveNeighbours(i, j)
                if board[i][j] & 1:
                    if count == 2 or count == 3:
                        board[i][j] |= (1 << 1)
                else: 
                    if count == 3:
                        board[i][j] |= (1 << 1)

        for i in range(ROWS):
            for j in range(COLS):
                board[i][j] >>= 1

    def gameOfLife2(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ROWS = len(board)
        COLS = len(board[0])
        temp = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        def countLiveNeighbours(r, c):
            count = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if(i < 0 or j < 0 or i >= ROWS or j >= COLS): continue
                    if((i,j) != (r,c) and board[i][j] == 1):
                        count += 1
            return count
        
        for i in range(ROWS):
            for j in range(COLS):
                count = countLiveNeighbours(i, j)
                if (board[i][j] and (count == 2 or count == 3)):
                    temp[i][j] = 1
                elif(board[i][j] and (count < 2 or count > 3)):
                    temp[i][j] = 0
                elif(board[i][j] == 0 and count == 3):
                    temp[i][j] = 1
        
        for i in range(ROWS):
            for j in range(COLS):
                board[i][j] = temp[i][j]

        



        