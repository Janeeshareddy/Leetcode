from math import ceil
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low=1
        high=max(piles)
        ans=high
        while low<=high:
            mid=(low+high)//2
            hours=0
            for i in piles:
                hours+=(i+mid-1)//mid
            if hours<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans