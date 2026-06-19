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
                if len(arr)==0 or i !=arr.pop():
                    return False
        if len(arr)>0:
            return False
        else:
            return True