class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1= {k:s.count(k) for k in s }
        d2= {k:t.count(k) for k in t }
        
        for i in d1:
            if (i not in d2) or (d1[i]!=d2[i]):
                return False
        return True