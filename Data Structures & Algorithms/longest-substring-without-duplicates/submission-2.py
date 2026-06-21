class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        max_len=0
        new_set=set()
        while r<len(s):
            if s[r] in new_set:
                max_len=max(max_len,r-l)
                l=r
                new_set=set()
            new_set.add(s[r])
            r+=1
        return max_len