class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d1= {k:s.count(k) for k in s }
        d2= {k:t.count(k) for k in t }
        
        return d1==d2