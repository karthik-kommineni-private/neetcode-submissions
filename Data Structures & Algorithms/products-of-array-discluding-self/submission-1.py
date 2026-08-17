class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #product  = left x right
        #1 2 4 6 -> 1, 1, 2, 6  * 48,24,6,1

        left, right = [1]*len(nums),[1]*len(nums)

        #left products
        for i in range(1,len(nums)):
            left[i] = left[i-1]*nums[i-1]

        #right producst
        for j in range(len(nums)-2,-1,-1):
            right[j] = nums[j+1]*right[j+1]

        return [a * b for a, b in zip(left, right)]  

"""
- idea : product is leftproduct * right product
- iteration always uses positive indices only 
"""
       


        