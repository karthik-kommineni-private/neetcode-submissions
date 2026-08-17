class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_length = float('-inf')
        curr_set = set()

        for r in range (len(s)):

            if s[r] in curr_set:
                l+=1
                continue
            curr_set.add(s[r])      
            max_length = max(max_length,r-l+1)
              

        return 0 if max_length == float('-inf') else max_length
        