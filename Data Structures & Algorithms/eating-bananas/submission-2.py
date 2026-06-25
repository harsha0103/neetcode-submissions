class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res=r
        while l <=r:
            mid=(l+r)//2
            hours=0
            for i in piles:
                hours+=math.ceil(float(i)/mid) 
            if h<hours:

                l=mid+1
            elif h>=hours:
                res=mid
                r=mid-1

        
        return res

