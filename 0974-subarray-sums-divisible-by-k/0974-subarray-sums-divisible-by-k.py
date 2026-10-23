class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix=0
        count=0
        freq={0:1}
        for num in nums:
            prefix+=num
            needed=prefix%k
            if needed in freq:
                count+=freq[needed]
            freq[needed]=freq.get(needed,0)+1
        return count