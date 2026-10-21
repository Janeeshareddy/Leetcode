class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positive=[]
        negative=[]
        for x in nums:
            if x>0:
                positive.append(x)
            else:
                negative.append(x)
        res=[]
        for i in range(len(nums)//2):
            res.append(positive[i])
            res.append(negative[i])
        return res