class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        freq={}
        for i in range(len(ransomNote)):
            freq[ransomNote[i]]=freq.get(ransomNote[i],0)+1
        for i in range(len(magazine)):
            if magazine[i] in freq:
                freq[magazine[i]]-=1
                if freq[magazine[i]]==0:
                    del freq[magazine[i]]   
        if len(freq)==0:
            return True
        else:
            return False        