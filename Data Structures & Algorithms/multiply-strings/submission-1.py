class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        l1=len(num1)
        l2=len(num2)
        res=[0]*(l1+l2)
        num1, num2 = num1[::-1], num2[::-1]

        for i in range(l1):
            for j in range(l2):
                temp= int(num1[i])*int(num2[j])
                res[i+j]+=temp
                res[i+j+1]+=res[i+j]//10
                res[i+j]=res[i+j]%10

        
        res=res[::-1]
        start=0
        
        for i in range(len(res)):
            if res[i]==0:
                start+=1
            else:
                break
        
        return ''.join(str(r) for r in res[start:])