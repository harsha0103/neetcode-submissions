class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if '0' in [num1,num2]:
            return '0'
        m,n=len(num1),len(num2)
        res=[0]*(len(num1)+len(num2))
        num1=num1[::-1]
        num2=num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                temp=int(num1[i])* int(num2[j])
                temp=res[i+j]+temp
                res[i+j+1]+=temp//10
                res[i+j]=temp%10
        

        res.reverse()
        i=0
        while i< len(res) and res[i]==0:
            i+=1
        
        res1=''.join(str(r) for r in res[i:])
        return res1