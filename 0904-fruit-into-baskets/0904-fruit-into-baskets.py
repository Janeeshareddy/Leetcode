class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left=0
        freq={}
        max_len=0
        for right in range(len(fruits)):
            freq[fruits[right]]=freq.get(fruits[right],0)+1
            if len(freq)>2:
                freq[fruits[left]]-=1
                if freq[fruits[left]]==0:
                    del freq[fruits[left]]
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len