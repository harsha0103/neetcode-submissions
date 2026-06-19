class Solution:
    def longestPalindrome(self, s: str) -> str:
        n= len(s)
        s1=s
        s2=s[::-1]

        dp=[['']*(n+1) for _ in range(n+1)]
        max_str=''

        def is_pal(string):
            i,j=0,len(string)-1
            while i<j:
                if string[i]!=string[j]:
                    return False
                i+=1
                j-=1
            return True

        for i in range(1,n+1):
            for j in range(1,n+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=s1[i-1]+dp[i-1][j-1]
                    if len(max_str)<=len(dp[i][j]) and is_pal(dp[i][j]):
                        max_str= dp[i][j]
        return  max_str
                    
