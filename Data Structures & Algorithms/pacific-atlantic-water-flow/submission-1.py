from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(r, c, visit, prev_height):
            # Stop if out of bounds, already visited, or height decreases
            if (
                r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r, c) in visit or heights[r][c] < prev_height
            ):
                return

            visit.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])

        # Pacific ocean (top row & left column)
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        # IMPROVEMENT: concise intersection using list comprehension
        return [[r, c] for (r, c) in pac if (r, c) in atl]




'''
Pacific Atlantic — Summary

1. Use reverse DFS from ocean borders instead of simulating flow from every cell.
2. Move to a neighbor only if its height is greater than or equal to the current cell.
3. Maintain two visited sets: one for Pacific and one for Atlantic.
4. Earlier mistake: starting DFS with a constant parent height (0) broke the height invariant.
5. Earlier mistake: DFS continued even when the height condition failed.
6. Correct approach enforces early return when height decreases.
7. Final result is the intersection of Pacific- and Atlantic-reachable cells.
8. Time Complexity: O(ROWS × COLS) — each cell visited at most twice.
9. Space Complexity: O(ROWS × COLS) — recursion stack and visited sets.
'''
