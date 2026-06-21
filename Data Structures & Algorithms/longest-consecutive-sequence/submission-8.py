class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        num_set= set(nums)
        longest=0
        done=set()
        for n in nums:
            if n-1 not in num_set:
                done.add(n)
                temp=1
                while n+1 in num_set:
                    temp+=1
                    n=n+1
                longest=max(temp,longest)
        return longest
                                
