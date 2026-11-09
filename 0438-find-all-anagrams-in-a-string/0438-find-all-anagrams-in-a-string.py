class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        freq={}
        need={}
        ans=[]
        k=len(p)
        for i in range(k):
            need[p[i]]=need.get(p[i],0)+1
        for i in range(len(s)):
            ch=s[i]
            freq[ch]=freq.get(ch,0)+1
            if i>=k:
                freq[s[i-k]]-=1
                if freq[s[i-k]]==0:
                    del freq[s[i-k]]
            if freq==need:
                ans.append(i-k+1)
        return ans  