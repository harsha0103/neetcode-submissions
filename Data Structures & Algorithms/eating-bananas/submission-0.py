class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start,end=1,max(piles)

        while start<= end:
            mid= start+(end-start)//2
            hours_spent=0
            for i in piles :
                hours_spent+=math.ceil(float(i)/mid)
            
            if hours_spent>h:
                start=mid+1
            else:
                end=mid-1
        return start