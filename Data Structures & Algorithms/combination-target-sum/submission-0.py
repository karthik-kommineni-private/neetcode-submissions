class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.nums = nums
        self.target = target
        self.dfs(0,[],0)
        return self.res


    def dfs(self,i, subset, curr_sum):
        if curr_sum == self.target:
            self.res.append(subset.copy())
            return
        if i >= len(self.nums) or curr_sum > self.target:
            return

        #choice 1 - consider number    
        subset.append(self.nums[i])
        curr_sum +=self.nums[i]
        self.dfs(i, subset, curr_sum)   #dfs(0,[2],0+2)
        
        #choice 2 - dont consider number 
        subset.pop()
        curr_sum-=self.nums[i]
        self.dfs(i+1, subset, curr_sum) #dfs(1,[],0)







"""
-

"""
        