class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF
        MASK = 0xFFFFFFFF

        for i in range(32):
            xor=a^b
            annd= (a&b)<<1

            a=xor
            b=annd
        
        return a  if a<MAX else ~(a^MASK)