class Solution(object):
    def subarraySum(self, nums, k):
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
            needed=prefix-k
            if needed in freq:
                count+=freq[needed]
            if prefix in freq:
                freq[prefix]+=1
            else:
                freq[prefix]=1
        return count