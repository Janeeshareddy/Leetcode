class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        last=[-1,-1,-1]
        count=0
        for i in range(len(s)):
            if s[i]=='a':
                last[0]=i
            elif s[i]=='b':
                last[1]=i
            else:
                last[2]=i
            count+=min(last)+1
        return count