from typing import List
from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        def hasCycle(node, parent):
            if node in visit:
                return True

            visit.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if hasCycle(nei, node):
                    return True
            return False

        # add edges one by one to know which edge creates the cycle
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

            visit = set()
            if hasCycle(u, -1):
                return [u, v]

        return []

'''
Redundant Connection — Summary

1. The graph starts as a tree and one extra edge introduces a cycle.
2. Edges are added one by one to identify which edge creates the cycle.
3. After each edge addition, DFS is used to check if a cycle exists.
4. A cycle is detected if a visited node is reached again (excluding parent).
5. The first edge that causes a cycle is the redundant connection.
6. Issue: for every edge addition, DFS is run again, leading to repeated traversals.
7. Time Complexity: O(n * (n + e)) — DFS is executed for each edge insertion.
8. Space Complexity: O(n + e) — adjacency list and DFS recursion stack.
'''
