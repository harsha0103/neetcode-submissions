class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=0
        d= {nums[i]:[target-nums[i],i] for i in range(len(nums))}

        for i in d:
            if d[i][0] in d:
                return [d[i][1],d[d[i][0]][1]]
            

