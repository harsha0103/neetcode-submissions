class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={0:1}
        res,curr_sum=0,0
    
        for i in range(len(nums)):
            curr_sum+=nums[i]
            diff=curr_sum-k
            if diff in d:
                res+=d[diff]
            if curr_sum in d:
                d[curr_sum]+=1       
            else:
                d[curr_sum]=1

        return res 