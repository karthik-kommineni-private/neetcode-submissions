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

        def hasCycle(node, parent):
            if node in visited:
                return True  # cycle detected

            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue  # ignore edge back to parent
                if hasCycle(nei, node):
                    return True
            return False

        # Check for cycle starting from node 0
        if hasCycle(0, -1):
            return False

        # Ensure graph is fully connected
        return len(visited) == n



'''
Valid Tree — Summary

1. A valid tree must have exactly n − 1 edges.
2. The graph must be undirected and fully connected.
3. Cycle detection in undirected graphs requires parent tracking.
4. Revisiting a node that is not the parent indicates a cycle.
5. DFS is used to traverse the graph and detect cycles.
6. Starting DFS from node 0 is sufficient if connectivity is checked.
7. Earlier mistake: used directed-graph cycle logic for an undirected graph.
8. Earlier mistake: skipped reverse edges, breaking the graph structure.
9. Time Complexity: O(n + edges).
10. Space Complexity: O(n + edges).
'''

