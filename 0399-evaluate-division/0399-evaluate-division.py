class Solution:
    def buildGraph(self, equations, values):
        graph = defaultdict(dict)

        for (s,t),v in zip(equations, values):
            graph[s][t] = v
            graph[t][s] = 1 / v
        
        return graph

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.buildGraph(equations, values)
        result = []

        for q in queries:
            s, t = q[0], q[1]
            
            if s not in graph or t not in graph:
                result.append(-1.0)
            
            elif s == t:
                result.append(1.0)
            
            else:
                result.append(self.bfs(graph, q))
        
        return result


    def bfs(self, graph, query):
        s, t = query[0], query[1]
        queue = deque([(s, 1)])
        seen = set()

        while queue:
            node, val = queue.popleft()

            if node in seen:
                continue

            for neighbour in graph[node]:
                res = graph[node][neighbour] * val

                if neighbour == t:
                    return res

                queue.append((neighbour, res))
                seen.add(node)        
        return -1.0




        
        