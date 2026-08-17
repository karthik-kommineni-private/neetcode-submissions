class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)
        max_len = 0

        for i in range(len(nums)):
            n = nums[i]
            if n-1 not in seen:
                length = 1
                while n+length in seen:
                    length +=1
                max_len = max(length,max_len)     
            else:
                continue 
                  
        return max_len
        



"""
- The elements do not have to be consecutive in the original array - hence we can use hashing
- start count only if its frist num in seq - means n-1 wont exists
- count increase as long as next number  exists
- dont have to see it as one list - 
seq can number exist or not is enough logic
"""