class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = self.getArea(i, j, grid)
                    print(area)
                    maxArea = max(area, maxArea)

        return maxArea

    def getArea(self, i, j, grid):
        if (i < 0 or i >= len(grid) 
            or j < 0 or j >= len(grid[0]) or grid[i][j] == 0):
            return 0

        grid[i][j] = 0
        area = 1

        area += self.getArea(i + 1, j, grid)
        area += self.getArea(i - 1, j, grid)
        area += self.getArea(i, j + 1, grid)
        area += self.getArea(i, j - 1, grid)

        return area