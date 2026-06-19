class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=[]
        borrow=1
        while digits:
            temp=digits.pop()
            temp+=borrow
            borrow=temp//10
            num=temp%10
            res.append(num)

        if borrow==1:
            res.append(borrow)
        
        res.reverse()
        return res