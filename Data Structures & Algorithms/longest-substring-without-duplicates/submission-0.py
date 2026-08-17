class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_length = float('-inf')
        curr_set = set()

        for r in range (len(s)):

            if s[r] in curr_set:
                max_length = max(max_length,r-l)
                curr_set.remove(s[r])
                l+=1

            curr_set.add(s[r])    

        return 0 if max_length == float('-inf') else max_length
        