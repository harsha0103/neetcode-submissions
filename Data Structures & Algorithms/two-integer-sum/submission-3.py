class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}

        for i,j in enumerate(nums):
            res=target-j
            if res in d:
                return [d[res],i]
            
            d[j]=i
        


    