class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        d = {}
        a = len(prices)-1
        while a>=0:
            if a == len(prices)-1:
                d[a] = prices[a]
            else: d[a] = max(d[a+1], prices[a])
            a-=1
        profit = 0
        for i,x in enumerate(prices):
            if d[i]-x > profit:
                profit = d[i]-x
        return profit