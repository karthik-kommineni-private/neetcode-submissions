class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        self.row_len, self.col_len = len(grid), len(grid[0])
        self.visit = set()
        return self.dfs(0, 0, grid)

    def dfs(self, r, c, grid) -> int:
        # base case
        if (
            r < 0 or c < 0 or
            r >= self.row_len or c >= self.col_len or
            (r, c) in self.visit or
            grid[r][c] == 1
        ):
            return 0

        if r == self.row_len - 1 and c == self.col_len - 1:
            return 1

        self.visit.add((r, c))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        count = 0

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            count += self.dfs(nr, nc, grid)

        self.visit.remove((r, c))
        return count
