class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        if len(nums) == 1:
            return nums[0]    
        #search max ele in search, next one is min
        i,j = 0, len(nums)-1

        while i<=j:
            m = (i+j)//2
            if m+1 <= len(nums)-1 and nums[m-1] >= 0:
                if nums[m-1]<nums[m]<nums[m+1]:
                    i = m+1
                else:
                    if nums[m+1] < nums[m]:
                        return nums[m+1]
                    else:
                        j = m-1


            if nums[m-1] == None:
                if nums[m] > nums[m+1]:
                    return nums[m+1]
                else:
                    return nums[m]    
            if nums[m+1] == None:
                if nums[m] > nums[m-1]:
                    return nums[m-1] 
                else:
                    return nums[m]        


                        
                










'''
find mid
4
6 nums[m+1] < nums[m] > nums[m-1]:
1




'''