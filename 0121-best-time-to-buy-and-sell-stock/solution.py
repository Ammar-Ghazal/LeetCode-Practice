class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time complexity: O(n)
        # Space complexity: O(1)
        
        # --------------- CLEANER IMPLEMENTATION ---------------
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit

        # --------------- FIRST IMPLEMENTATION ---------------
        # # sliding window problem, use 2 ptrs
        # maxProfit = 0
        # l, r  = 0,1 #left is buy, right is sell
        # # keep running the loop, until we reach the last value with r
        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         maxProfit = max(maxProfit, profit)
        #     else: #if we find a new low price, set it as the left ptr
        #         l=r
        #     # always increment the right ptr
        #     r+=1
        # return maxProfit
