class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #target =0, i,j,k not equal, no duplicates in solution
        res = []
        target = 0
        nums.sort() #brutefore -o(n3) - we want in n2 - sorted -o(nlogn)


        for i,n in enumerate(nums):
            #i>0 to avoid index out of range
            if i and (nums[i] == nums[i-1]):   
                continue

            j,k = i+1, len(nums)-1

            while j < k:
                s = nums[j] + nums[k] + nums[i]
                if s == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1 #move
                    k -= 1
                    # skip duplicates on both sides
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif s > 0:
                    k-=1
                else:
                    j+=1


        return res                    
                      


        