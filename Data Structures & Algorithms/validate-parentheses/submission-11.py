class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]

        for i in s: 
            if i =='(' or i=='{' or i=='[':
                arr.append(i)
            else:
                res=arr.pop()
                if (i==')' and res!='(') or (i=='}' and res!='{') or (i==']' and res!='[') :
                    return False
        return True
                    