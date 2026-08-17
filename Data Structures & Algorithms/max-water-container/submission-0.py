class Solution:
    def maxArea(self, h: List[int]) -> int:

        # v = r-l * min(l,r)
        #move smaller

        max_vol = 0
        l,r = 0, len(h)-1

        while l < r:
            min_h = min(h[l], h[r])
            max_vol = max(max_vol, (r-l)* min_h)

            if min_h == h[r]:
                r-=1
            else:
                l+=1

        return max_vol            


        