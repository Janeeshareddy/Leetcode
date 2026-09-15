class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini_price=prices[0]
        max_profit=0
        for price in prices:
            mini_price=min(mini_price,price)
            profit=price-mini_price
            max_profit=max(max_profit,profit)
        return max_profit