class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        res.append(1)

        for i in range(1,len(nums)):
            #res(1) = nums(0)* res(0)
            res.append(nums[i-1]*res[i-1])

        prod = 1
        for i in range(len(nums)-2,-1,-1):
            prod = prod*nums[i+1]
            res[i] = res[i]*prod

        return res        





        