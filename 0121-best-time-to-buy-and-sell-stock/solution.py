class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        lowestBuy = prices[0]
        maxProfit = 0

        for p in prices:
            lowestBuy = min(p, lowestBuy)
            maxProfit = max(p - lowestBuy, maxProfit)

        return maxProfit
