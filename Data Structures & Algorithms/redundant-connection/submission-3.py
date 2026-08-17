class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # For every node, parent is initially itself
        par_map = {i: i for edge in edges for i in edge}
        # Rank represents size of the component
        rank = {j: 1 for edge in edges for j in edge}

        def find(curr_node):
            # Find root parent
            curr_par = par_map[curr_node]
            if curr_par != curr_node:
                par_map[curr_node] = find(curr_par)
            return par_map[curr_node]

        def union(n1, n2):
            # Root representatives
            p1, p2 = find(n1), find(n2)
            r1, r2 = rank[p1], rank[p2]

            # Cycle detected
            if p1 == p2:
                return False

            # Union by rank (size)
            if r1 > r2:
                par_map[p2] = p1
                rank[p1] += rank[p2]
            elif r2 > r1:
                par_map[p1] = p2
                rank[p2] += rank[p1]
            else:
                par_map[p2] = p1
                rank[p1] += rank[p2]

            return True

        # Process edges in order
        for x, y in edges:
            if not union(x, y):
                return [x, y]
'''
Redundant Connection — Summary

1. The graph starts as a tree and one extra edge introduces a cycle.
2. Edges are processed one by one to identify which edge creates the cycle.
3. Union-Find (Disjoint Set Union) is used to track connected components.
4. Each node initially belongs to its own component.
5. `find` uses path compression to optimize parent lookup.
6. `union` merges components using rank (size) optimization.
7. If two nodes already share the same root, a cycle is detected.
8. That edge is the redundant connection and is returned immediately.
9. Issue in DFS approach: for every edge, DFS was executed repeatedly.
10. Time Complexity: O(e α(n)) — near constant per edge due to Union-Find optimizations.
'''
