class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        ans=0
        freq={}
        for right in range(len(s)):
            if s[right] in freq and freq[s[right]]>=left:
                left=freq[s[right]]+1
            freq[s[right]]=right
            ans=max(ans,right-left+1)
        return ans