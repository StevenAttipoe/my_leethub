class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROW, COL = len(matrix), len(matrix[0])
        markedRows, markedCols = set(), set()
        
        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j] == 0:
                    markedRows.add(i)
                    markedCols.add(j)
                    
            
        for i in range(ROW):
            for j in range(COL):
                if i in markedRows or j in markedCols:
                    matrix[i][j] = 0
                    

                    
                    
        