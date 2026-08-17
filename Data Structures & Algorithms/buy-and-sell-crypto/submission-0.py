class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy low, sell high
        l,r = 0,1
        max_profit = 0

        for r in range(len(prices)):
            if prices[l] < prices[r]: #if small value found
                profit = prices[r] - prices[l]
                max_profit = max(profit,max_profit)
            else:
                l = r
        return max_profit     










"""
-bf,opt,edge, dry
-buy low, sell high
- iterate to find the lowest till that point and compare it with all values aftre it



"""       
        