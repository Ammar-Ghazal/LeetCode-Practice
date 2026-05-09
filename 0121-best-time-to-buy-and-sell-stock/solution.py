class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # ------------- Cleaner Implementation --------
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        maxProfit = 0
        lowestBuyPrice = prices[0]

        for p in prices:
            lowestBuyPrice = min(p, lowestBuyPrice)
            maxProfit = max(p-lowestBuyPrice, maxProfit)
        
        return maxProfit

        # ------------- Implementation #1 -------------
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # maxProfit = 0
        # l,r = 0,0

        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r]-prices[l]
        #         maxProfit = max(maxProfit, profit)
        #     else:
        #         l = r
        #     r+=1

        # return maxProfit

