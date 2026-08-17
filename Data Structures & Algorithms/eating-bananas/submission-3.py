class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high = 1, max(piles)
        result = 0   # NOTE: could also initialize to high for clarity (since answer always exists)

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
        sum = 0   # NOTE: shadows built-in 'sum', better to rename to 'total'
        for p in piles:
            sum = sum+ math.ceil(p/bph)
        return sum          



'''
Problem type:
→ Binary Search on Answer (search space is speed, not index)

Core idea:
→ We are searching minimum valid speed
→ As speed increases → required hours decreases (monotonic)

Search space:
→ low = 1
→ high = max(piles)

Approach:
1. mid = candidate speed
2. Compute hours needed at this speed
3. If hours <= h:
   → valid → store result → try smaller (high = mid - 1)
4. Else:
   → too slow → increase speed (low = mid + 1)

Helper:
→ cal_r(speed, piles) = sum of ceil(pile / speed)

Important:
- Monotonic function enables binary search
- Always store result when valid
- Ceil ensures correct hour calculation

Mistakes / things to watch:
- Using 'sum' shadows built-in (not breaking, but avoid)
- Make sure condition is monotonic before applying BS
- result initialized to 0 works, but high is safer default

Complexity:
→ Time: O(n log max(piles))
→ Space: O(1)

Mental model:
ANSWER SPACE → CHECK VALID → SHRINK LEFT TO MINIMIZE
'''