class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total=1
        zeros=0
        for i in nums:
            if i !=0:
                total*=i
            else:
                zeros=1

        res=[]

        for i in nums:
            if zeros==1:
                if i !=0:
                    res.append(0)
                else:
                    res.append(total)
            else:
                res.append(total//i)
        return res
