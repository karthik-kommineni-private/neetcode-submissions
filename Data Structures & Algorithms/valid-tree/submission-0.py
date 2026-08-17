from typing import List
from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False  # cycle detected

            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue  # ignore edge back to parent
                if not dfs(nei, node):
                    return False
            return True

        # Check for cycles starting from node 0
        if not dfs(0, -1):
            return False

        # Ensure graph is fully connected
        return len(visited) == n
