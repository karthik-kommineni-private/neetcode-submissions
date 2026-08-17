class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high = 1, max(piles)
        result = 0

        while low<=high:
            mid = (low+high)//2
            rate = self.cal_r(mid,piles) 
            if rate <= h:
                result = mid
                high = mid-1
            else:
                low = mid+1
        return result


    def cal_r(self, bph, piles):
        sum = 0
        for p in piles:
            sum = sum+ math.ceil(p/bph)
        return sum          





'''
-1 to,max. of arr -> range
- mid = 
- compare mid hours with h
- fundtion calculate_height(arr,1)

- chek =
- low = 23, high = 25 - 6
- mid = 24


'''
        