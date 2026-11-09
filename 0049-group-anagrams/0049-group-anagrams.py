class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        freq={}
        for ch in strs:
            key="".join(sorted(ch))
            if key not in freq:
                freq[key]=[]
            freq[key].append(ch)
        return freq.values()