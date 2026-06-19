class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        max_len=0
        new_set=set()
        while r<len(s):
            while s[r] in new_set:
                new_set.remove(s[l])
                l+=1
            max_len=max(max_len,r-l+1)
            new_set.add(s[r])
            r+=1
        return max_len