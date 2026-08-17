class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        max_len = 0
        count= {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0)+1
            #every substring - calculate len if its valid
            if (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)

        return max_len    


        