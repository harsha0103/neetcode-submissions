from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1=defaultdict(int)

        for i in s:
            d1[i]+=1

        for i in t:
            if i in d1:
                d1[i]-=1
            else:
                return False

        return sum(d1.values())==0