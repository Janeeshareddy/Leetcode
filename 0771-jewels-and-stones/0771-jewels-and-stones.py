class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewel_set=set(jewels)
        count=0
        for x in stones:
            if x in jewel_set:
                count+=1
        return count