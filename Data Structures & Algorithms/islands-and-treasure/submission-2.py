class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        visit = set()

        def helper(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == -1 or (r, c) in visit:
                return INF

            if grid[r][c] == 0:
                return 0

            visit.add((r, c))

            min_count = min(
                helper(r, c - 1),
                helper(r, c + 1),
                helper(r - 1, c),
                helper(r + 1, c)
            )

            visit.remove((r, c))

            if min_count == INF:
                return INF

            return 1 + min_count

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = helper(r, c)



'''
- issue is dfs can't reach all cells if there is no way hence for loops are required
- general dfs time is 4^mn -> now at every cell -> mn 4^mn


'''
