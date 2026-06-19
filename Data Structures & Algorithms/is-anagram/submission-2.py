class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1= {}
        d2= {}
        
        for i in s:
            if i in d1:
                d1[i] = 1+ d1[i]
            else:
                d1[i]=0
        for i in t:
            if i in d2:
                d2[i] = 1+ d2[i]
            else:
                d2[i]=0
        return d1==d2