class Solution:
    def countSubstrings(self, s: str) -> int:
        dp={}
        pal={}
        n=len(s)
        def is_pal(i,j):
            if (i,j) in pal:
                return pal[(i,j)]
            l,r=i,j
            while l<r:
                if s[l]!=s[r]:
                    pal[(i,j)]=False
                    return False
                l+=1
                r-=1
            pal[(i,j)]=True
            return pal[(i,j)]
        
        def dfs(i):
            if i==len(s):
                return 0
            
            if i in dp:
                return dp[i]
            count=0
            for j in range(i,n): 
                if is_pal(i,j):
                    count+=1
            
            dp[i]=count+dfs(i+1)

            return dp[i]
        
        return dfs(0)


