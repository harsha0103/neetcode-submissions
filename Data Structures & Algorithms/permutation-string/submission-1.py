class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1=defaultdict(int)
        d2=defaultdict(int)

        for i in s1:
            d1[i]+=1
        
        n1,n2=len(s1),0
        l=0
        for r in range(len(s2)):
            if n1==n2:
                if d1==d2:
                    return True
                else:
                    d2[s2[l]]-=1
                    n2-=1
                    l+=1

            
            n2+=1
            d1[s2[r]]
            d2[s2[r]]+=1
        return d1==d2