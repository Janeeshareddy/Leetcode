class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        chars=set()
        answer=0
        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left+=1
            chars.add(s[right])
            answer=max(answer,right-left+1)
        return answer