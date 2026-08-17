class Solution:
    def trap(self, heights: List[int]) -> int:
        #+ve,
        l,r = 0, len(heights)-1

        left_max,right_max,water = heights[l],heights[r],0

        while l < r:

            if left_max < right_max:
                water += left_max - heights[l]
                l+=1
                left_max = max(heights[l],left_max)
            else:
                water += right_max - heights[r]
                r-=1
                right_max = max(heights[r],right_max)

        return water        











"""


"""
        