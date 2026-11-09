class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        d1={}
        d2={}
        for i in range (len(s)):
            a=s[i]
            b=t[i]
            if a in d1 and d1[a]!=b:
                return False
                # break
            if b in d2 and d2[b]!=a:
                return False
                # break
            d1[a]=b
            d2[b]=a
        return True