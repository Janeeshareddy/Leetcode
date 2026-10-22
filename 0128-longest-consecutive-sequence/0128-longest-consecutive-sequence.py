class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best=0
        arr=set(nums)
        for x in arr:
            if x-1 not in arr:
                current=x
                count=1
                while current+1 in arr:
                    current+=1
                    count+=1
                best=max(best,count)
        return best
        