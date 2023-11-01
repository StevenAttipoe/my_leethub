class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        towers = [[0] * i for i in range(1, query_row + 2)]
        towers[0][0] = poured

        for i in range(query_row):
            for j in range(len(towers[i])):
                excess = (towers[i][j] - 1) / 2
                if excess > 0:
                    towers[i + 1][j] += excess
                    towers[i + 1][j + 1] += excess

        return min(1, towers[query_row][query_glass])
        

        
        