class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        n, m = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in directions:
                i, j = r + dr, c + dc
                if (0 <= i < n and 0 <= j < m and (i, j) not in visited
                        and heights[r][c] <= heights[i][j]):
                    dfs(i, j, visited)

        for r in range(n):
            dfs(r, 0, pacific)
            dfs(r, m - 1, atlantic)


        for c in range(m):
            dfs(0, c, pacific)
            dfs(n - 1, c, atlantic)

        return pacific & atlantic
                    



        

         




            