class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        freq={}
        need={}
        k=len(s1)
        for i in range(len(s1)):
            need[s1[i]]=need.get(s1[i],0)+1
        for i in range(len(s2)):
            freq[s2[i]]=freq.get(s2[i],0)+1
            if i>=k:
                freq[s2[i-k]]-=1
                if freq[s2[i-k]]==0:
                    del freq[s2[i-k]]
            if freq==need:
                return True
                break
        return False