class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res=[]
        substr=[]

        def dfs(i):
            if i>len(s)-1:
                res.append(substr[:])
                return
            
            for j in range(i,len(s)):
                if self.ispal(i,j,s):
                    substr.append(s[i:j+1])
                    dfs(j+1)
                    substr.pop()
        dfs(0)
        return res
        
    def ispal(self,start,end,string):
        while start<end:
            if string[start]!=string[end]:
                return False
            start+=1
            end-=1
        return True