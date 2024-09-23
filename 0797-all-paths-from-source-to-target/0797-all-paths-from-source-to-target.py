class Solution:
    # O(2^N * N) time
    # O(N) space
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        target = len(graph) - 1

        def dfs(node, path):
            if node == target:
                paths.append(path[:])
                return

            for neighbour in graph[node]:
                path.append(neighbour)
                dfs(neighbour, path)
                path.pop()
            
        dfs(0, [0])
        return paths

