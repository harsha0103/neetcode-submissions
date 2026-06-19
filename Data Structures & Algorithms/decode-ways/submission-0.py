class Solution:
    def numDecodings(self, s: str) -> int:
        mapping= set()
        for i in range(1,27):
            mapping.add(str(i))
        
        dp={}
        def dfs(i):

            if i== len(s):
                return 1
            
            if i in dp:
                return dp[i]
            if s[i]=='0':
                return 0

            count=0
            if s[i] in mapping:
                count+=dfs(i+1)
            if i+1 <len(s) and s[i:i+2] in mapping:
                count+=dfs(i+2)
                
            dp[i]=count
            return count
        return dfs(0)
            


        