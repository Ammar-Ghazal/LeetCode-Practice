class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # For both implementations:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        maxProfit = 0
        lowestBuyPrice = prices[0]

        for p in prices:
            lowestBuyPrice = min(p, lowestBuyPrice)
            maxProfit = max(p-lowestBuyPrice, maxProfit)
        
        return maxProfit


        # First Implementation:
        # buy, maxProfit = 0, 0

        # for sell in range(len(prices)):
        #     if prices[sell] > prices[buy]:
        #         curProfit = prices[sell] - prices[buy]
        #         maxProfit = max(curProfit, maxProfit)
        #     else:
        #         buy = sell
        
        # return maxProfit
