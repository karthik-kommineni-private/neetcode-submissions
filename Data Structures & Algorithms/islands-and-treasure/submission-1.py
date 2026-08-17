from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        visit = set()
        #dfs - improved
        def helper(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == -1 or (r, c) in visit:
                return INF

            if grid[r][c] == 0:
                return 0

            # Already computed
            if grid[r][c] != INF:
                return grid[r][c]

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

            grid[r][c] = 1 + min_count
            return grid[r][c]

        # DFS must be triggered for each land cell
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    helper(r, c)




