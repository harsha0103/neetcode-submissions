class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        substr=set()
        res=0
        while j<len(s):
            while  s[j] in substr:
                substr.remove(s[i])
                i+=1
               
            substr.add(s[j])
            res=max(res,j-i+1)
            j+=1
            
        return res
   
        while r<len(s):
            while s[r] in new_set:
                new_set.remove(s[l])
                l+=1
            max_len=max(max_len,r-l+1)
            new_set.add(s[r])
            r+=1
        return max_len