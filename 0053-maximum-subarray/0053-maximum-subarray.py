class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            current=max(nums[i],current+nums[i])
            ans=max(ans,current)
        return ans