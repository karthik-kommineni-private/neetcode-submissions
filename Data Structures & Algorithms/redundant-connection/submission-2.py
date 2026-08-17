class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par_map = {i:i for edge in edges for i in edge} #for every node par is itself
        rank = {j:1 for edge in edges for j in edge} #height is 1 for all

        #find parent
        def find(curr_node):
            # Direct parent of the current node
            curr_par = par_map[curr_node] 
            if curr_par != curr_node:                 # Move upward until a root node is reached
                curr_par = find(curr_par)
            return curr_par





        def union(n1,n2):
            p1, p2 = find(n1), find(n2)
            r1, r2 = rank[p1], rank[p2]
            if p1 == p2:
                return False

            if r1>r2:
                par_map[p2] = p1
            elif r2>r1:
                par_map[p1] = p2
            else:
                par_map[p2] = p1
                rank[p1] += rank[p2]
            return True    



        for x,y in edges:
            if union(x,y):
                continue
            return [x,y]    

