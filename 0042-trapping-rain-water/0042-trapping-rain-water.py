class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        left_max=0
        right_max=0
        water=0
        while left<right:
            left_max=max(left_max,height[left])
            right_max=max(right_max,height[right])
            if left_max < right_max:
                water=water+left_max-height[left]
                left+=1
            else:
                water=water+right_max-height[right]
                right-=1
        return water
