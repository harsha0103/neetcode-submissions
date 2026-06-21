class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        wordSet=set(wordDict)

        dp=[0]* (n+1) 
        
        for i in range(1,n+1):
            for j in range (i):
                if s[j:i] in wordSet:
                    dp[i]=1
                    break 
        print(dp)
        return sum(dp)==len(wordSet)