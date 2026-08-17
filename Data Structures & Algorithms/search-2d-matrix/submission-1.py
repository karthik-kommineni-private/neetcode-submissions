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


    def simple_binary_search(self, nums: List[int], target: int) -> bool:
        l,r = 0, len(nums)-1 
        while l <= r: 
            mid = l+((r-l)//2)
            if target == nums[mid]: 
                return True
            elif target >nums[mid]:
                l = mid+1
            else:
                r = mid-1

        return False        



        