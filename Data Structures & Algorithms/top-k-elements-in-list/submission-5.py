class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d= defaultdict(int)

        for i in nums:
            d[i]+=1
        res=[[] for _ in range(len(nums)+1)]
        for key,val in d.items():
            res[val].append(key)
        
        final=[]
        while k>0:
            if len(res[-1])==0:
                res.pop()
                continue 
            
            else:
                temp=res[-1].pop()
                final.append(temp)
                k-=1
        return final