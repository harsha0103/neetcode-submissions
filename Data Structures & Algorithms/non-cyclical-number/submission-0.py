class Solution:
    def isHappy(self, n: int) -> bool:
        visited=set()

        def square(n):
            res=0
            while n:
                t=n%10
                res+=t*t
                n=n//10
            return res

        while n not in visited:
            visited.add(n)
            n=square(n)
            if n==1:
                return True
        return False


        