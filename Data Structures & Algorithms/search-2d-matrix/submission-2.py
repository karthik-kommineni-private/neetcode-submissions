class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #first find the row which has value using modified bs
        firstRow, lastRow = 0, len(matrix)-1

        while firstRow <= lastRow:
            midRow = (firstRow+lastRow)//2
            #last element in midRow
            if target > matrix[midRow][-1]: 
                firstRow = midRow+1
            elif target < matrix[midRow][0]:   
                lastRow = midRow-1
            else:
                return self.simple_binary_search(matrix[midRow],target)
        return False # if value is not found in midRow #Target not in range of any row

    def simple_binary_search(self, nums: List[int], target: int) -> bool:
        l,r = 0, len(nums)-1 
        while l <= r: 
            mid = l+((r-l)//2)   # NOTE: good practice to avoid overflow (even though Python handles it)
            if target == nums[mid]: 
                return True
            elif target >nums[mid]:
                l = mid+1
            else:
                r = mid-1

        return False        



'''
Problem type:
→ Binary Search on 2D matrix (treated as sorted rows)

Core idea:
→ Each row is sorted AND
→ First element of a row > last element of previous row

So:
→ Matrix behaves like a flattened sorted array
→ But we can do it in 2 steps instead of flattening

Approach:
1. Binary search on rows:
   - Check if target lies within row range:
     matrix[midRow][0] <= target <= matrix[midRow][-1]

2. If target fits in row:
   → Run normal binary search on that row

3. If target > last element of row:
   → move down (firstRow = midRow + 1)

4. If target < first element:
   → move up (lastRow = midRow - 1)

Important:
- Use row boundaries (first + last element) to eliminate rows
- Second binary search is standard
- Early return when correct row is found

Mistakes / things to watch:
- Ensure matrix is non-empty before accessing (edge case)
- Be careful with matrix[midRow][-1] and [0] (valid indexing)
- Don’t overcomplicate by flattening unless needed

Complexity:
→ Time: O(log m + log n)
→ Space: O(1)

Mental model:
2D MATRIX → PICK CORRECT ROW → APPLY NORMAL BINARY SEARCH
'''