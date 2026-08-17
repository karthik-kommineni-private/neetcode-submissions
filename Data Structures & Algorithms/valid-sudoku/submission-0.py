class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows_map = collections.defaultdict(set)
        col_map = collections.defaultdict(set)
        sq_map = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.': continue
                if (board[r][c] in rows_map[r] or board[r][c] in col_map[c] 
                or board[r][c] in sq_map[(r//3,c//3)]):
                    return False

                rows_map[r].add(board[r][c])
                col_map[c].add(board[r][c])
                sq_map[(r//3,c//3)].add(board[r][c])

        return True        


        