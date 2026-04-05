class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        
        if days == 0:
            return 0
        
        l, r, max_profit, min_price = 0, 0, 0, prices[0]
        
        while r < days and l <= r:
            if prices[r] < min_price:
                min_price = prices[r]
                l = r + 1
            max_profit = max(max_profit, prices[r]-min_price)
            r = r + 1

        return max_profit
            
            
