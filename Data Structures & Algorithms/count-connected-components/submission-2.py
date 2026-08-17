class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        n_map = defaultdict(list)

        for i,j in edges:
            n_map[i].append(j)
            n_map[j].append(i)

        visit = set()

        def dfs(node,parent):
            if node in visit:
                return
            visit.add(node)
            for n in n_map[node]:
                if n == parent:
                    continue
                dfs(n,node) 


        count = 0
        for node in range(n):
            if node in visit:
                continue
            count +=1    
            dfs(node,-1)   

        return count


'''
Number of Connected Components — Summary

1. Build an undirected graph using an adjacency map.
2. Use DFS to traverse and mark all nodes in one connected component.
3. Maintain a visited set to avoid revisiting nodes.
4. Each new DFS call from an unvisited node represents a new component.
5. Parent tracking prevents unnecessary backtracking in undirected graphs.
6. Count is incremented only when starting DFS from an unvisited node.
7. Time Complexity: O(n + e) — O(e) for adjacency/map traversal and O(n) since each node is visited once during DFS.
8. Space Complexity: O(n + e) — adjacency list and recursion stack.
'''
