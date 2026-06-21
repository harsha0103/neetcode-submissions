class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=1
        indicator=''
        res_lis=[]
        for i in nums:
            if i !=0:
                res=res*i
            else:
                indicator="zero"
        
        for i in nums:
            if i !=0:
                if indicator =='zero':
                    res_lis.append(0)
                else:
                    res_lis.append(res//i)
            else:
                res_lis.append(res)
        return res_lis

        

        