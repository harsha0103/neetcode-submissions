class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=1
        c=0
        res_lis=[]
        for i in nums:
            if i !=0:
                res=res*i
            else:
                c+=1
        if len(nums)==c:
            return nums
        
        for i in nums:
            if i !=0:
                if c !=0:
                    res_lis.append(0)
                else:
                    res_lis.append(res//i)
            else:
                if c>1:
                    res_lis.append(0)
                else:
                    res_lis.append(res)
        return res_lis

        

        