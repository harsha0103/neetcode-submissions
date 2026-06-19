from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        res=[]
        b=1
        while digits:
            curr=digits.pop()
            curr+=b
            if curr<9:
                digits.append(curr)
                return digits+res
            
            b=curr//10
            num=curr%10
            res=[num]+res
        return [b]+res if b>0 else res