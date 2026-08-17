class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res






"""
[[]]
# dfs(0,nums) - [[],[1]]
# dfs(1,nums)  - [], [1], [2] [1,2]
#dfs(2,nums). - [],[1],[2],[1,2][3][1,3]1,2,3
"""



        