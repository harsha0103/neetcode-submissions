from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        d1=defaultdict(int)
        d2=defaultdict(int)

        for i in s1:
            d1[i]+=1
        
        n1=len(s1)
        n2=0

        l=0

        for r in range(len(s2)):
            n2+=1
            d2[s2[r]]+=1
            d1[s2[r]]

            if n2==n1:
                if d1==d2:
                    return True
                d2[s2[l]]-=1
                l+=1
                n2-=1
        return False
        