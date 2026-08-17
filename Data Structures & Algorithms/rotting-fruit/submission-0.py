class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1    


        while fresh > 0 and q:
            for _ in range(len(q)):
                r,c = q.popleft()

                directions = [(0,1),(0,-1),(1,0),(-1,0)]

                for dr, dc in directions:
                    nr,nc = dr+r, dc+c

                    if nr< 0 or nc <0 or nr >= ROWS or nc >= COLS or ((nr,nc) in visit) or grid[nr][nc] == 0:
                        continue

                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh -=1

            time+=1

        return time if fresh == 0 else -1    



'''
Use multi-source BFS starting from all rotten oranges (2), since the problem asks for minimum time.

Treat each BFS level as 1 minute, incrementing time only after processing the current level.

Update the grid in place (1 → 2) to mark oranges as rotten; this removes the need for a separate visit set.

Track the count of fresh oranges and reduce it as they rot to know when to stop.

Stop BFS when either no fresh oranges remain or no more cells can be processed.

❌ Earlier mistake: incremented time even when no fresh orange rotted (off-by-one error).

❌ Earlier mistake: used a redundant visit set instead of relying on the grid state.

Time Complexity: O(ROWS × COLS) — each cell is processed at most once.

Space Complexity: O(ROWS × COLS) — queue may hold all cells in the worst case.


'''

        