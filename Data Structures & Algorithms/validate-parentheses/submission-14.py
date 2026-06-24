class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        mapping={']':'[', '}':'{',')':'('}

        for i in s: 
            if i =='(' or i=='{' or i=='[':
                arr.append(i)
            else:
                if len(arr)==0:
                    return False
                res=arr.pop()
                if res in mapping :
                    return False
        return True if len(arr)==0 else False
                    