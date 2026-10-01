class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]

        for sellPrice in prices:
            maxProfit = max(maxProfit, sellPrice - minBuy)
            minBuy = min(minBuy, sellPrice)
        
        return maxProfit