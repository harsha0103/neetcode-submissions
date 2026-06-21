class Solution:
    def checkValidString(self, s: str) -> bool:
        def dfs(i,lopen):
            if i==len(s):
                return lopen==0
            
            if s[i]=='(':
                return dfs(i+1,lopen+1)
            
            elif s[i]==')':
                return dfs(i+1,lopen-1)
            else:
                return (dfs(i+1,lopen) or 
                dfs(i+1,lopen+1) or
                dfs(i+1,lopen-1))
        
        return dfs(0,0)