#graph, story,time
#ite-end,seen - all excl, dfs-all direction, if water true
class Solution:
    def __init__(self):
        self.row_len = 0
        self.col_len = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        self.row_len = len(grid)
        self.col_len = len(grid[0])
        seen = set()
        count = 0
        for r in range(self.row_len):
            for c in range(self.col_len):
                if grid[r][c] == "1" and (r,c) not in seen:
                    isIsland = self.dfs(r,c,grid,seen)
                    if isIsland:
                        count +=1
        return count                


    def dfs(self,r,c,grid,seen):
        #basecase - bounds, isIsland
        if min(r,c) < 0:
            return True
        if r == self.row_len or c == self.col_len:
            return True
        if (r,c) in seen:
            return True        
        if grid[r][c] == "0":
            return True

        seen.add((r,c))

        left = self.dfs(r,c-1,grid,seen)
        right = self.dfs(r,c+1,grid,seen)
        top = self.dfs(r+1,c,grid,seen)
        bottom = self.dfs(r-1,c,grid,seen) 

        return left and right and top and bottom


        