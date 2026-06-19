class Solution:
    def isValid(self, s: str) -> bool:
        mapping={']':'[', '}':'{',')':'('}
        new_lis=list(s)
        updated=[]
        while new_lis:
            current=new_lis.pop()

            if current in mapping:
                updated.append(mapping[current])
            else:
                if len(updated)==0:
                    return False
                res=updated.pop()
                if res!=current:
                    return False
        return len(updated)==0

