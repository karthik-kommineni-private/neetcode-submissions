class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visit = set()


        def dfs(r,c):
            if (c<0 or r<0) or (c>=COLS or r>=ROWS):
                return 0
             
            if (board[r][c] == "X") or (r,c) in visit:
                return 1
            # if 0 change to X - to know visited
            visit.add((r,c))

            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            final_res = 1
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                final_res = final_res*dfs(nr,nc)    
            if final_res == 1:  
                board[r][c] = "X" 

            return final_res    


        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    dfs(i,j)

'''

Mistakes Summary — Previous Approach (Surrounded Regions)

1. Tried to decide flip vs no-flip per cell instead of making a region-level decision.
2. Used DFS return values (0/1) and arithmetic to infer enclosure, which is fragile and non-standard.
3. Treated out-of-bounds as failure, even though touching the border means the region is safe.
4. Mutated the board during DFS before confirming the entire region was enclosed.
5. Made the solution order-dependent by mixing traversal and mutation.
6. Started DFS from every 'O', causing repeated work and inconsistent behavior.
7. Did not explicitly handle border-connected 'O' cells, which is the core invariant.
8. Mixed traversal, decision-making, and mutation in one DFS, violating separation of concerns.
9. Relied on DFS return semantics instead of marking safe cells.

Key Lesson:
This problem is about protecting border-connected regions, not evaluating individual cells.
'''
