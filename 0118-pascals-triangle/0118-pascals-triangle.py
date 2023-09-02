class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for r in range(numRows):
            row = [None for i in range(r + 1)]
            row[0] = row[-1] = 1

            for c in range(1, len(row) - 1):
                row[c] = triangle[r - 1][c - 1] + triangle[r - 1][c]

            triangle.append(row)

        return triangle
        