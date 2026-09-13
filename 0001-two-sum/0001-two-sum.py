class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j         #O(n^2)
        # left=0
        # right=len(nums)-1
        # while left<right:
        #     sum=nums[left]+nums[right]
        #     if sum==target:
        #         return left,right
        #     elif sum<target:
        #         left+=1
        #     else:
        #         right-=1
        # return[-1,-1]
