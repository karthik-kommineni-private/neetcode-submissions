class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len = 0

        for r in range(1,len(s)):
            if s[r] != s[l]:
                if k>0:
                    max_len = max(r-l+1,max_len)
                    k-=1   
                else:
                    l=r
                    k=k    
            else:            
                max_len = max(r-l+1,max_len)

        return max_len    


"""
k

"""









"""
set - if substring is distinct
k is like a counter
when seq breaks - do count,max count, update l = r


"""
        