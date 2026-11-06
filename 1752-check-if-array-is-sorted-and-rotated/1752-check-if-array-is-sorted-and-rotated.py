class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sortedNums = sorted(nums)
        arr = []
        for i in range(len(nums)):
            arr.insert(0, sortedNums.pop())
            if nums == arr + sortedNums:
                return True
        return False
