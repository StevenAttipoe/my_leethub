"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        def dfs(cur, visited):
            deepCopy = Node(cur.val)
            visited[deepCopy.val] = deepCopy

            for neighbour in cur.neighbors:
                if neighbour.val not in visited:
                    deepCopy.neighbors.append(dfs(neighbour, visited))
                else:
                    deepCopy.neighbors.append(visited[neighbour.val])

            return deepCopy
        
        return dfs(node, {})

