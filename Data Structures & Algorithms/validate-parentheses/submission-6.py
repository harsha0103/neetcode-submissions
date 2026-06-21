class Solution:
    def isValid(self, s: str) -> bool:
        
        d={'(':')','{':'}','[':']'}
        stack=[]

        for param in s:
            if param in d:
                stack.append(d[param])
            else:
                temp=stack.pop()
                if  temp!=param:
                    return False
        return len(stack)==0