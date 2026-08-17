class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            seen.add(num)
        return not len(nums) == len(seen)    

         