class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d= defaultdict(int)

        for i in nums:
            d[i]+=1
        
        res=[]
        for i in d:
            if d[i]>=k:
                res.append(i)
        return res
        