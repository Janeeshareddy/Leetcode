class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        def nb(bloomDay,mid,m,k):
            count=0
            no=0
            for i in range(len(bloomDay)):
                if(bloomDay[i]<=mid):
                    count+=1
                else:
                    no+=count//k
                    count=0
            no+=count//k
            if no>=m:
                return True
            else:
                return False
        low=min(bloomDay)
        high=max(bloomDay)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if(nb(bloomDay,mid,m,k)==True):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans