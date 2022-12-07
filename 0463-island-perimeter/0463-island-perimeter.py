class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def islandPerimeterHelper(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return 1
            elif grid[i][j] == 0:
                return 1
            elif grid[i][j] == -1:
                return 0
            else:
                grid[i][j] = -1
                
                return  islandPerimeterHelper(i + 1, j) + islandPerimeterHelper(i - 1, j) + \
                        islandPerimeterHelper(i, j + 1)  + islandPerimeterHelper(i, j - 1) 

        ROW, COL = len(grid), len(grid[0])
        
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    return islandPerimeterHelper(i, j)