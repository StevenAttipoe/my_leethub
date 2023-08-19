class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        n, m = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prevHeight):
            if(r < 0 or c < 0 or r >= n or c >= m 
                or prevHeight > heights[r][c] or (r,c) in visited):
                return

            visited.add((r, c))

            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(m):
            dfs(0, c, pacific, heights[0][c])
            dfs(n - 1, c, atlantic, heights[n - 1][c])

        for r in range(n):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, m - 1, atlantic, heights[r][m - 1])

        return pacific & atlantic
                    



        

         




            