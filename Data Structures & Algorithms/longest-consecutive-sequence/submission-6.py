class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        snums=set(nums)
        longest=0

        for i in nums:
            if i-1 not in snums:
                length=0
                while i+length in snums:
                    length+=1
                longest=max(length,longest)
            if longest>len(nums)//2:
                return longest 
        return longest
