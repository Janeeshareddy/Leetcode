class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        ssum=0
        for i in range(k):
            ssum+=nums[i]
        max_sum=ssum
        for i in range(k,len(nums)):
            ssum=ssum-nums[i-k]+nums[i]
            max_sum=max(max_sum,ssum)
        return float(max_sum)/k