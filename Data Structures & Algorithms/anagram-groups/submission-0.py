class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)

        #for c in strs :
        #        d[''.join(sorted(c))].append(c)
        #return d.values()
        
        for c in strs:
            tup=[0]*26
            for i in c:
                tup[ord(i)-ord('a')]+=1
            d[tuple(tup)].append(c)
        return d.values()

            