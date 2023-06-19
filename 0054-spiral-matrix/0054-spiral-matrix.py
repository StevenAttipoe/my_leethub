class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1

        order = []
        while left <= right and top <= bottom:
            # Move left to right
            for i in range(left, right + 1):
                order.append(matrix[top][i])
            top += 1

            #Move top to bottom
            for i in range(top, bottom + 1):
                order.append(matrix[i][right])
            right -= 1

            #Move right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    order.append(matrix[bottom][i])
                bottom -= 1

            #Move bottom to top:
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    order.append(matrix[i][left])
                left  += 1
        return order





