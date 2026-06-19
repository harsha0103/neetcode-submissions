class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res=[]
        subset=[]
        candidates.sort()
        def dfs(i,target1):

            if target==target1:
                res.append(subset[:])
                return 
            if i >len(candidates)-1 or target1>target:
                return 

            
            subset.append(candidates[i])
            dfs(i+1,target1+candidates[i])

            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i=i+1
            
            subset.pop()
            dfs(i+1,target1)
        

        dfs(0,0)
        return res 

        