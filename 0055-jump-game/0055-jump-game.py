class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        gas=0
        for item in nums:
            if gas<0:
                return False
            if item>gas:
                gas=item
            gas-=1
        return True