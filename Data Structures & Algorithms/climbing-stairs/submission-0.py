class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [1,1]
        for step in range(2,n+1):
            ways.append(ways[step-1] + ways[step-2])

        return ways[n]    


    




'''
2- 2
3 - f(2) + 1
4 - f(3) + 1. -- 1+1+1+1, 1+1+2, 2+1+1, 2+2
5-  1+1+1+1+1, 1+1+2+1, 2+1+1+1, 2+2+1, 1+2+1+1, 1+2+2, 2+1+2


'''
        