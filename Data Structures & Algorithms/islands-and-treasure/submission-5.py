class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        INF = 2147483647
        ROWS,COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        count = 0
        

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visit.add((i,j))

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                directions = [(0,1),(0,-1),(1,0),(-1,0)]
                #move all directions and add eligible nei in q  
                for dr, dc in directions:
                    nr, nc = dr+r, dc+c

                    if min(nr,nc)<0 or (nr == ROWS or nc == COLS) or (grid[nr][nc] == -1) or ((nr,nc) in visit):
                        continue
                    if grid[nr][nc] == INF:
                        grid[nr][nc] = count+1
                        q.append((nr,nc))
                        visit.add((nr,nc))
            count+=1            
                    
'''
### 📝 Revision Notes (Matching Your Code)

- **Multi-source BFS**: All gates (`0`) are enqueued first and added to the `visit` set.
- **Level-order traversal**: Processing `len(q)` nodes per iteration maps each BFS layer to one distance.
- **Visited tracking with `visit`**: The `visit` set prevents revisiting cells already processed.
- **Distance using `count`**: `count` represents the current BFS level and is incremented after each layer.
- **Neighbor validation**: Out-of-bounds cells, walls (`-1`), and visited cells are skipped.

### ⏱ Time Complexity
- **O(R × C)** — each cell is visited and processed at most once during BFS.

### 💾 Space Complexity
- **O(R × C)** — the queue and the `visit` set together may store all grid cells in the worst case.


'''         

                    









        