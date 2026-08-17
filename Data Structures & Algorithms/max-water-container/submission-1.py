class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #heights of bars, max vol - max(length of short bar out of two x width)

        l,r = 0, len(heights)-1
        max_vol = 0

        while l<r:
            vol = min(heights[l],heights[r])*(r-l)
            if heights[l] < heights[r]:  #only changin shorter length can increase vol
                curr_height = heights[l]
                l +=1
                new_height = heights[l]
                while l < r and new_height <= curr_height:
                    l+=1
            else:
                curr_height = heights[r]
                r-=1
                new_height = heights[r]
                while l < r and new_height <= curr_height:
                    r-=1
            max_vol = max(vol,max_vol) 
        return max_vol            

           


# vol - 1*7, max - 7 - l+
# vol - 6*6 max -36 - r-,r-






"""
-bf, optz, edge,dryrun
- bf - o(n2) - eliminate few case with two pointer
- move pointer on shorter side because potential to increase 
vol by decreasing width is when height is more
- search for taller height

"""

