class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subsets = [[]]
        self.dfs(0,nums)
        return self.subsets

    
    
    def dfs(self, i, nums):
        if i >= len(nums):
            return
        
        new_subsets = []
        for val in self.subsets:       # iterate over old subsets
            new_subsets.append(val + [nums[i]])  # build new ones
        
        self.subsets.extend(new_subsets)  # add them all at once
        self.dfs(i+1, nums)






"""
[[]]
# dfs(0,nums) - [[],[1]]
# dfs(1,nums)  - [], [1], [2] [1,2]
#dfs(2,nums). - [],[1],[2],[1,2][3][1,3]1,2,3
"""



        