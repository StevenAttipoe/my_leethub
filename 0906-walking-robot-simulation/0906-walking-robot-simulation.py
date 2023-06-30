class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dy = [1, 0, -1, 0]
        dx = [0, 1, 0, -1]
        x = y = 0
        di = 0
        obstacleSet = { (a, b) for a, b in obstacles }
        maxDistance = 0

        for value in commands:
            if value == -1:
                di = (di + 1) % 4
            elif value == -2:
                di = (di - 1) % 4
            else:
                for k in range(value):
                    if (x+dx[di], y+dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        distance = x**2 + y**2
                        maxDistance = max(maxDistance, distance)

        return maxDistance
        


        