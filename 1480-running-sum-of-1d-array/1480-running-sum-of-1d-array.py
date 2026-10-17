class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
      ans=[]
      rsum=0
      for i in range(len(nums)):
        rsum=rsum+nums[i]
        ans.append(rsum)
      return ans