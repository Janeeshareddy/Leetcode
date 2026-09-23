class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atmost(k):
            if k<0:
                return 0
            left=0
            count=0
            ans=0
            for right in range(len(nums)):
                count+=nums[right]%2
                while count>k:
                    count-=nums[left]%2
                    left+=1
                ans+=right-left+1
            return ans
        return atmost(k)-atmost(k-1)