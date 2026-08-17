from typing import List

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
                if grid[r][c] == "1" and (r, c) not in seen:
                    self.dfs(r, c, grid, seen)
                    count += 1  # new island found
        return count

    def dfs(self, r, c, grid, seen):
        # OUT OF BOUNDS
        if r < 0 or c < 0 or r >= self.row_len or c >= self.col_len:
            return

        # WATER
        if grid[r][c] == "0":
            return

        # ALREADY VISITED
        if (r, c) in seen:
            return

        # MARK VISITED
        seen.add((r, c))

        # EXPLORE ALL 4 DIRECTIONS
        self.dfs(r, c - 1, grid, seen)   # left
        self.dfs(r, c + 1, grid, seen)   # right
        self.dfs(r - 1, c, grid, seen)   # up
        self.dfs(r + 1, c, grid, seen)   # down


# Why this solution is better:
# - Uses correct DFS flood-fill: dfs() does not return booleans; it only marks connected land.
# - Proper guard clauses: stop on out-of-bounds, water, or visited cells, keeping logic predictable.
# - Correct visited handling: (r, c) coordinates stored in 'seen', preventing reprocessing.
# - Clean separation of concerns: numIslands() counts islands; dfs() only explores one island.
# - Fixes earlier logical issues (wrong visited checks, wrong returns, no-op count increment).
# Overall, this version follows standard graph traversal practices, is easier to reason about,
# and guarantees correct results with optimal time complexity.