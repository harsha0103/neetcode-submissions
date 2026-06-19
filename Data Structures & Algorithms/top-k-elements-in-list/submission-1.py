class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d= defaultdict(int)
        ma=0
        res=[]

        for i in nums:
            d[i]+=1
            ma=max(ma,d[i])
        
        d1=defaultdict(list)
        for ke,v in d.items():
            d1[v].append(ke)
        
        while k>0:
            if ma in d1:
                res.extend(d1[ma])
                k=k-len(d1[ma])
            ma-=1
        return res
        