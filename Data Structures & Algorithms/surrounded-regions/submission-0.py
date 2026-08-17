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

        