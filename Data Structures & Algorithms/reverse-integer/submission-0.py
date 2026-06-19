class Solution:
    def reverse(self, x: int) -> int:
        neg=1
        if x<0:
            neg=-1
        res=0
        x=abs(x)
        while x>0:
            temp= x%10
            res=res*10+temp
            x=x//10
        
        res=res*neg
        if -2**31 <= res <=2**31-1:
            return res
        else:
            return 0
