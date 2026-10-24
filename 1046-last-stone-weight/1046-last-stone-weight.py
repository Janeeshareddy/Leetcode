class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones=[-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            first=-(heapq.heappop(stones))
            second=-(heapq.heappop(stones))
            if first!=second:
                heapq.heappush(stones,-(first-second))
        if stones:
            return -stones[0]
        return 0