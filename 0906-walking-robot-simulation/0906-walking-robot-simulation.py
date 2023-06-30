class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = { (a, b) for a, b in obstacles }
        max_dist = 0

        facing = (0, 1)
        x, y = 0, 0

        for value in commands:
            if value == -2: #left
                facing = (-facing[1], facing[0])
            elif value == -1: #right
                facing = (facing[1], -facing[0])
            else:
                for _ in range(value):
                    nx = x + facing[0]
                    ny = y + facing[1]

                    if (nx, ny) in obstacle_set:
                        break

                    x, y = nx, ny
            dist = x*x + y*y
            max_dist = max(max_dist, dist)
        
        return max_dist


        