class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(set) # row_num: set of values
        col_map = defaultdict(set) # col_num: set of values
        box_map = defaultdict(set) # box_num: set of values

        for i in range(9):
            for j in range(9):
                curr_val = board[i][j]
                if curr_val == ".":
                    continue  # Skip empty cells
                box_num = (i//3)*3 + (j//3)
                if curr_val in row_map[i] or curr_val in col_map[j] or curr_val in box_map[box_num]:
                    return False

                row_map[i].add(curr_val)     
                col_map[j].add(curr_val)  
                box_map[box_num].add(curr_val)    

        return True






"""
- box_num is calculated based on row number and column number box_num = (i//3)*3 + (j//3)
- i//3 will give if - top,middle,bottom row
- j//3 will give if - top,middle,bottom col
- *3 shifts to the correct row in the flattened 1D array of boxes
"""