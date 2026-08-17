class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [1,1]
        for step in range(2,n+1):
            ways.append(ways[step-1] + ways[step-2])

        return ways[n]    

'''
Climbing Stairs — Summary

1. This is a classic dynamic programming problem.
2. To reach step n, you can come from step n−1 or n−2.
3. The recurrence relation is f(n) = f(n−1) + f(n−2).
4. Base cases: f(0) = 1 and f(1) = 1.
5. DP array stores number of ways to reach each step.
6. Using append avoids index-out-of-bounds errors.
7. The solution builds results bottom-up.
8. Time Complexity: O(n) — O(n) iterations since each step is computed once.
9. Space Complexity: O(n) — DP array stores results for all steps.
'''

    




'''
2- 2
3 - f(2) + 1
4 - f(3) + 1. -- 1+1+1+1, 1+1+2, 2+1+1, 2+2
5-  1+1+1+1+1, 1+1+2+1, 2+1+1+1, 2+2+1, 1+2+1+1, 1+2+2, 2+1+2


'''
        