from collections import defaultdict
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(i):
            if i >=len(nums):
                return [[]]

            res_set=[]
            perm=dfs(i+1)

            for p in perm:
                for j in range(len(p)+1):
                    c=p[:]
                    c.insert(j,nums[i])
                    res_set.append(c)
            return res_set
        res=dfs(0)
        dic=defaultdict(int)
        for r in res:
            dic[tuple(r)]+=1
        final_res=[]
        for key in dic:
            final_res.append(list(key))
        return final_res
