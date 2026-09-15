class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        windows_sum=sum(nums[:k])
        answer=windows_sum
        for i in range(k,len(nums)):
            windows_sum+=nums[i]
            windows_sum-=nums[i-k]
            answer=max(answer,windows_sum)
        return float(answer)/k