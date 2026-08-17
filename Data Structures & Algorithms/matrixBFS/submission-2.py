class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        #len, g[0][0] -> grid[4][4]. len
        rows_len, col_len = len(grid), len(grid[0])
        curr_len = 0
        visit = set()
        q = deque()
        q.append((0,0))
        visit.add((0,0))
    

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                # visit.add((r,c)). - also correct but may repeat adds
                if r == rows_len - 1 and c == col_len - 1:
                    return curr_len

                #this for loop is to just add neighbours
                directions = [(0,1), (0,-1), (1,0), (-1,0)]
                for dr,dc in directions:
                    nr,nc = dr+r, dc+c
                    if ((min(nr,nc)<0) or 
                        nr >= rows_len or nc >= col_len or
                        (r + dr, c + dc) in visit or
                        grid[nr][nc] == 1):
                        continue    
                    
                    q.append((nr,nc)) #add only valid neighbours
                    visit.add((nr,nc))
            curr_len+=1

        return -1


        