class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0

        for length in range(1, n + 1):  # length of substring
            for i in range(0, n - length + 1):
                j = i + length - 1  # end index

                if s[i] == s[j]:
                    if length <= 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        res += 1

        return res
