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
