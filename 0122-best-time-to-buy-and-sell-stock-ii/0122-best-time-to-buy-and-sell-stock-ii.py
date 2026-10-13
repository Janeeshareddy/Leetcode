class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans=0
        n=len(prices)
        for i in range(1,n):
            if prices[i]>=prices[i-1]:
                ans+=prices[i]-prices[i-1]
        return ans