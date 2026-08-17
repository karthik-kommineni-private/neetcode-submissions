class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        ROWS, COLS = len(heights), len(heights[0])
        atl, pac = set(), set() #if a cell flows to atl - add

        #check neighbours - will they flow to respective ocean
        def dfs(r,c,visit, parentHeight):
            if min(r,c) < 0 or (r>= ROWS or c>=COLS) or (r,c) in visit or heights[r][c] < parentHeight:
                return 
            visit.add((r,c))
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            for dr, dc in directions:
                dfs(dr+r,dc+c, visit,heights[r][c])
            

        for i in range(ROWS):
            dfs(i,0,pac, 0)
            dfs(i, COLS-1,atl,0)

        for j in range(COLS):
            dfs(0,j,pac,0)
            dfs(ROWS-1, j,atl,0)  

        for ar,ac in atl:
                if ((ar,ac) in pac):
                    res.append([ar,ac])

        return res            




    

        