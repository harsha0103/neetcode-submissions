class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h_set=set()
        l=0
        max_len=float('-inf')
        for r in range(len(s)):
            if s[r] in h_set:
                while s[l]!=s[r]:
                    h_set.remove(s[l])
                    l+=1 
                h_set.remove(s[l])
                l+=1
                
            h_set.add(s[r])
            max_len=max(max_len,r-l+1)
        return max_len if max_len != float('-inf') else 0
            

        