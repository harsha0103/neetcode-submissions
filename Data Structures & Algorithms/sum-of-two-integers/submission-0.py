class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        for i in range(32):
            xor=a^b
            annd= (a&b)<<1

            a=xor
            b=annd
        
        return a