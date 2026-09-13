class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # l=len(height)
        # max_area=0
        # for i in range(l):
        #     for j in range(i+1,l):
        #         width=j-i                                     #O(n^2)
        #         h=min(height[i],height[j])
        #         area=width*h
        #         max_area=max(max_area,area)
        # return max_area
        n=len(height)
        l=0
        r=n-1
        ans=0
        area=0
        while l<r:
            area=(r-l)*min(height[l],height[r])
            ans=max(area,ans)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return ans