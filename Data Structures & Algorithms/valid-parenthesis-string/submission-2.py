class Solution:
    def checkValidString(self, s: str) -> bool:
        dp={}
        def dfs(i,lopen):
            if i==len(s):
                return lopen==0
            
            if lopen<0:
                return False
            
            if (i,lopen) in dp:
                return dp[(i,lopen)]
            
            if s[i]=='(':
                dp[(i,lopen)]=dfs(i+1,lopen+1)
                return dp[(i,lopen)]
            
            elif s[i]==')':
                dp[(i,lopen)]=dfs(i+1,lopen-1)
                return dp[(i,lopen)]
            else:
                dp[(i,lopen)]= (dfs(i+1,lopen) or 
                dfs(i+1,lopen+1) or
                dfs(i+1,lopen-1))
                return dp[(i,lopen)]
        
        return dfs(0,0)