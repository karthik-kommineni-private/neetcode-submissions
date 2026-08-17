class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        max_len = 0
        l = 0
        counter = [0]*26
        max_count_so_far = 0
        if len(s) == 1: return 1


        for r in range(len(s)):
            counter[ord(s[r]) - ord('A')] +=1
            max_count_so_far = max(max_count_so_far,counter[ord(s[r]) - ord('A')])

            if((r-l+1) - max_count_so_far > k):
                counter[ord(s[l]) - ord('A')] -=1
                l+=1

        return max(max_len,r-l+1)
            
            


        