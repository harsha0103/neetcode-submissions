class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1= defaultdict(int)
        d2= defaultdict(int)
        
        for i in s:
            d1[i] = 1+ d1[i]
        for i in t:
            d2[i] = 1+ d2[i]
        return d1==d2