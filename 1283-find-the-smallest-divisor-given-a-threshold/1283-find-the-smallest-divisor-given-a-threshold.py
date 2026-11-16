class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def check(nums,t):
                ans=0
                for j in range(len(nums)):
                    ans+=(nums[j]+mid-1)//mid
                if(ans<=t):
                    return True
                else:
                    return False
        low=1
        high=max(nums)
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            if(check(nums,threshold)==True):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans