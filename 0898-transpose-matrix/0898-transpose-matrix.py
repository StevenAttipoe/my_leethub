class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(matrix), len(matrix[0])
        
        ans = [[None] * ROW for _ in range(COL)]

        for r in range(ROW):
            for c in range(COL):
                ans[c][r] =  matrix[r][c]

        return ans
