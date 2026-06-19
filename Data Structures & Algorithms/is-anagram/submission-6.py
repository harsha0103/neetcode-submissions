from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        test1,test2=defaultdict(int),defaultdict(int)
        for i in s:
            test1[i]+=1
        for j in t:
            test2[j]+=1
        return test1==test2
        