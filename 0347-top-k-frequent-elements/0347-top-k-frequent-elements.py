class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq={}
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
        items=sorted(freq,key=lambda x:freq[x],reverse=True)
        return items[:k]