""" Problem 121. Best Time to Buy and Sell Stock
    Author: Artur Gasparyan
    Date: 12 Jan 2023
    Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/876703923/
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Track smallest number and optimal pair
        # Go from left to right
        # If pair between smallest number and current is better than optimal pair, store this instead

        max_profit = 0
        min_investment = prices[0]

        for price in prices[1:]:
            profit = price - min_investment
            if profit > max_profit:
                max_profit = profit

            if price < min_investment:
                min_investment = price

        return max_profit