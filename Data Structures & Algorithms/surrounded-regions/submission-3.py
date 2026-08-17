from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        q = deque()

        # 1) Enqueue all border 'O's and mark them safe
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
                    if board[r][c] == "O":
                        board[r][c] = "#"
                        q.append((r, c))

        # 2) BFS to mark all 'O's connected to border as safe
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == "O":
                    board[nr][nc] = "#"
                    q.append((nr, nc))

        # 3) Flip enclosed regions and restore safe cells
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"

'''
Surrounded Regions — Summary

1. A region of 'O' should be flipped only if it does NOT touch the border.
2. Start BFS from all border 'O' cells to mark them as safe.
3. Any 'O' connected to a border 'O' must not be flipped.
4. Safe cells are temporarily marked to avoid reprocessing.
5. After BFS, flip all remaining 'O' cells to 'X'.
6. Restore safe cells back to 'O'.
7. Earlier mistake: tried to decide flip per cell instead of per region.
8. Earlier mistake: mixed traversal and mutation inside DFS/BFS.
9. Time Complexity: O(ROWS × COLS) — each cell processed once.
10. Space Complexity: O(ROWS × COLS) — queue in worst case.



'''