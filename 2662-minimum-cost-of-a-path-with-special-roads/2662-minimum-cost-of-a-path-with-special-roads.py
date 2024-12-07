class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def costTo(self, other: "Point") -> int:
        return abs(other.x - self.x) + abs(other.y - self.y)
    
    def __repr__(self):
        return f"Point({self.x},{self.y})"

    def __lt__(self, other: "Point"):
        if self.x < other.x: return True
        elif self.x == other.x and self.y < other.y: return True
        return False

class Solution:
    def buildGraph(self, specialRoads):
        graph = []

        for sr in specialRoads:
            x1, y1, x2, y2, c = sr

            p1 = Point(x1, y1)
            p2 = Point(x2, y2)

            if p1.costTo(p2) < c:
                continue

            graph.append((p1, p2, c))
        return graph
        
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        specialRoads = self.buildGraph(specialRoads)

        start = Point(start[0], start[1])
        target = Point(target[0], target[1])

        minCost = start.costTo(target)
        seen, heap = set(), [(0, start)]
        
        while heap:
            cost, node = heappop(heap)

            if node in seen or cost > minCost:
                continue
            
            seen.add(node)
            minCost = min(minCost, cost + node.costTo(target))

            for s,t,c in specialRoads:
                heappush(heap, (cost + node.costTo(s) + c,t))

        return minCost