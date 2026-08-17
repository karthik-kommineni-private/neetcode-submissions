class Solution:
    def findMin(self, nums: List[int]) -> int:
        # sorted, unique
        # len(num) - rotate - 
        #BS - criteria - ele rigth > left

        l,r = 0,len(nums)-1
        while l<=r:
            mid = (r+l)//2
            if nums[mid-1]>nums[mid]<nums[mid+1]:
                return nums[mid]
            elif nums[l]>nums[mid]: #idealy first ele < mid, if not - found arr with ele
                r = mid - 1
            else:
                l = mid+1

        return -1        











"""
trick - find the dip element - means a element for which next is small
-  l < mid < r
- decide side - first ele in left_arr is smaller than last ele in arr  

- bf- optm(sort,search,hasmap,stack,heap,tree),edge, dry

"""