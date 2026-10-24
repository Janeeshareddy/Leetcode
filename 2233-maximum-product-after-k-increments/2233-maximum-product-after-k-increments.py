class Solution(object):
    def maximumProduct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        for i in range(k):
            smallest=heapq.heappop(nums)
            heapq.heappush(nums,smallest+1)
        ans=1
        for x in nums:
            ans=(ans*x)%(10**9+7)
        return ans