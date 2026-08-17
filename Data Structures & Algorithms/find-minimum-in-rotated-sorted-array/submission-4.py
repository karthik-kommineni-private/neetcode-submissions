class Solution:
    def findMin(self, nums: List[int]) -> int:
        # sorted, unique
        # len(num) - rotate - 
        #BS - criteria - ele rigth > left
        
        l,r = 0,len(nums)-1
        if nums[l] <= nums[r]:  # Early exit: no rotation
            return nums[l]
        while l<=r:
            mid = (r+l)//2
          # dip at mid (safe left check)
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]

            # dip right after mid (safe right check)
            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if nums[l]>nums[mid]: #idealy first ele < mid, if not - found arr with ele
                r = mid - 1
            else:
                l = mid+1

        return -1        











"""
trick - find the dip element - means a element for which next is small
-  l < mid < r
- decide side - first ele in left_arr is smaller than last ele in arr  

- bf- optm(sort,search,hasmap,stack,heap,tree),edge(index outofbound, nullpointer), dry

"""