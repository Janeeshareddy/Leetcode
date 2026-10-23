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
            ch=s[right]
            if ch in freq and freq[ch]>=left:
                left=freq[ch]+1
            freq[ch]=right
            ans=max(ans,right-left+1)
        return ans