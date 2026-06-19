class Solution:
    def longestPalindrome(self, s: str) -> str:
        n= len(s)
        s1=s
        s2=s[::-1]

        dp=[[0]*(n+1) for _ in range(n+1)]
        pal_len=0
        end_index=0



        for i in range(1,n+1):
            for j in range(1,n+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                    if pal_len<=dp[i][j]:
                        string1=i-dp[i][j]
                        string2=n-j
                        if string1==string2:
                            pal_len= dp[i][j]
                            end_index=i

        return  s[end_index-pal_len:end_index]
                    
