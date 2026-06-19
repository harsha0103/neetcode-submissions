class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=defaultdict(int)
        for n in nums:
            d[n]+=1
        res=[]

        for i,j in d.items():
            res.append([j,i])
        
        res.sort()
        final=[]
        while k>0:
            i,v=res.pop()
            final.append(v)
            k-=1
        return final