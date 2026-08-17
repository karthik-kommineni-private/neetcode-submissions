class Solution:
    def findMin(self, nums: List[int]) -> int:
        i,j = 0, len(nums)-1

        while i < j:
            m = (i+j)//2
            mid = nums[m]
            left = nums[i]
            right = nums[j]

            if mid > right:
                i = m+1
            else:
                j = m

        return nums[j]           


        