class Solution:
    def isValid(self, s: str) -> bool:
        
        d={'(':')','{':'}','[':']'}
        stack=[]

        for param in s:
            if param in d:
                stack.append(d[param])
            else:
                if not stack or  stack.pop()!=param:
                    return False
        return len(stack)==0