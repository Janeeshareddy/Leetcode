class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        freq={}
        for i in range(len(s)):
            freq[s[i]]=i
        start=0
        end=0
        result=[]
        for i in range(len(s)):
            end=max(end,freq[s[i]])
            if i==end:
                result.append(end-start+1)
                start=i+1
        return result