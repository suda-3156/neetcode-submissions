class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sell = 0
        profit = 0

        while sell < len(prices):
            while sell < len(prices) and prices[sell] >= prices[buy]:
                profit = max(profit, prices[sell] - prices[buy])
                sell += 1

            buy += 1
        
        return profit