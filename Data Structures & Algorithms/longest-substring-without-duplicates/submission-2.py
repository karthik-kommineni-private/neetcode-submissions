class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #end window - no repeating char, maxlen
        l,r = 0,0
        seen = set()
        max_length = 0

        for r in range(len(s)):
            while s[r] in seen: #while because 
                seen.remove(s[l])
                l+=1
                continue
            seen.add(s[r])
            max_length = max(max_length,r-l+1)     

        return max_length    








"""
- move l when window breaks and adjust for the movmt

"""
        