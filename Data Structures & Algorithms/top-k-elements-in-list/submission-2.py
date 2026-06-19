class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}

        res = [[] for _ in range(len(nums)+1)]
        res1=[]
        for i in nums:
            d[i] = (d[i] + 1) if i in d else 1

        for key, v in d.items():
            res[v].append(key)
        
        for i in range(len(res)-1,-1,-1):
            for j in res[i]:
                if k>0:
                    res1.append(j)
                    k-=1
                else:
                    return res1
        return res1