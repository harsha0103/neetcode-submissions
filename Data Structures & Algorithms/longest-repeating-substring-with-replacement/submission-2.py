from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i,j=0,0
        new_dict=defaultdict(int)
        max_len=0
        while j<len(s):
            new_dict[s[j]]+=1

            if (j-i+1)-max(new_dict.values())>k:
                new_dict[s[i]]-=1
                i+=1
            
            max_len=max(max_len,j-i+1)
            j+=1
        
        return max_len