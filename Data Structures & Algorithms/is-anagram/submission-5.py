from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1=defaultdict(int)

        for i in s:
            d1[i]+=1

        for i in t:
            d1[i]-=1

        for i in d1:
            if d1[i]!=0:
                return False
        return True