class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0] * i for i in range(1, query_row + 2)]
        tower[0][0] = poured

        for i in range(query_row):
            for j in range(len(tower[i])):
                excess = (tower[i][j] - 1) / 2
                if excess > 0:
                    tower[i + 1][j] += excess
                    tower[i + 1][j + 1] += excess

        return min(1, tower[query_row][query_glass])
        

        
        