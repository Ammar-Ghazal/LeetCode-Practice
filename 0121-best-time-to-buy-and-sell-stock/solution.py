class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window problem, use 2 ptrs
        # Time complexity: O(n)
        # Space complexity: O(1)
        
        maxProfit = 0
        l, r  = 0,1 #left is buy, right is sell

        # keep running the loop, until we reach the last value with r
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else: #if we find a new low price, set it as the left ptr
                l=r
            # always increment the right ptr
            r+=1
        return maxProfit
