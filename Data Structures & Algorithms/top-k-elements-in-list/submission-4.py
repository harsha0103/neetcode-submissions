class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d= defaultdict(int)

        for i in nums:
            d[i]+=1
        res=[]
        for i,v in d.items():
            res.append((v,i))
        
        res.sort()
        print(res)
        final=[]
        while k>0:
            x,y=res.pop()
            final.append(y)
            k-=1
        return final