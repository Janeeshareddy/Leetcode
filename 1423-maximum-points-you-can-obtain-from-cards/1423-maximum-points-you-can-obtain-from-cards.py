class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        leftsum=0
        for i in range(k):
            leftsum+=cardPoints[i]
        ans=leftsum
        right=len(cardPoints)-1
        for i in range(k-1,-1,-1):
            leftsum=leftsum-cardPoints[i]+cardPoints[right]
            right-=1
            ans=max(ans,leftsum)
        return ans