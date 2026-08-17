class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)  #O(n)
        max_len = 0

        for i in range(len(nums)):
            if (nums[i]-1) not in nums_set:
                #its a start
                length = 1
                while nums[i]+length in nums_set:
                        length +=1  

                max_len = max(max_len,length)        


        return max_len