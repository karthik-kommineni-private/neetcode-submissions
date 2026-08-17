class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        n_map = defaultdict(list)

        for i,j in edges:
            n_map[i].append(j)
            n_map[j].append(i)

        visit = set()

        def dfs(node,parent):
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
        