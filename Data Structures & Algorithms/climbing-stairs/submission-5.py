class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n<=2:
            return n
        
        arr=[1,2]
        i=2
        while i<=n:
            temp=arr[1]
            arr[1]=sum(arr)
            arr[0]=temp
            i+=1
        return arr[0]