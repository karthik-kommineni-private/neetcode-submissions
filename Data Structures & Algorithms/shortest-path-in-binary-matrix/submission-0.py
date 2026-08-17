from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # fail fast: start or end blocked
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        queue = deque([(0, 0, 1)])
        visited = set([(0, 0)])

        while queue:
            r, c, length = queue.popleft()

            # reached destination
            if r == n - 1 and c == n - 1:
                return length

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # ----- boundary check -----
                if nr < 0 or nc < 0 or nr >= n or nc >= n:
                    continue

                # ----- blocked or visited -----
                if grid[nr][nc] == 1 or (nr, nc) in visited:
                    continue

                visited.add((nr, nc))
                queue.append((nr, nc, length + 1))

        return -1


