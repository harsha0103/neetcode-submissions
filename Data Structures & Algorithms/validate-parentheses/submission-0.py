class Solution:
    def isValid(self, s: str) -> bool:
        
        d={'(':')','{':'}','[':']'}
        arr=[]

        if len(s)%2!=0:
            return False
        
        for i in s:
            if i in d:
                arr.append(d[i])
            else:
                if len(arr)==0 or arr.pop()!=i:
                    return False
        return len(arr)==0