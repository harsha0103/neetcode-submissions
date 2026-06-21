from collections import Counter
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        d=Counter(hand)
        min_arr=[]
        for key in d:
            heapq.heappush(min_arr,(key,d[key]))
        print(min_arr)
        prev=0
        res=[]
        while min_arr:
            curr,count=heapq.heappop(min_arr)
            if len(res)>1 and curr-prev!=1:
                return False
            prev=curr
            if len(res)==groupSize:
                while res:
                    new,new_count=res.pop()
                    if new_count>0:
                        heapq.heappush(min_arr,(new,new_count))
                prev=0
            res.append((curr,count-1))
        return True