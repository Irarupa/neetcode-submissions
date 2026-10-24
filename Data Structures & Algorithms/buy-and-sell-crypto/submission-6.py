class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        maxp = 0
        profit = 0

        for price in prices:
            profit = price-minp

            if profit>maxp:
                maxp = profit
            if price<minp:
                minp = price
        return maxp

