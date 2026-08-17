class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for x in matrix:
            result = self.search(x,target)
            if result == True: 
                return True
        return False        





    def search(self, nums: List[int], target: int) -> bool:
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
        