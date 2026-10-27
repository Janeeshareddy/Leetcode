class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        s=sorted(set(arr))
        ans=[]
        freq={}
        for i in range(len(s)):
            freq[s[i]]=i+1
        for x in arr:
            ans.append(freq[x])
        return ans