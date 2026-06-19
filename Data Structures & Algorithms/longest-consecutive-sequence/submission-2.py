class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=list(sorted(nums))
        if not len(nums):
            return 0
        count=0
        max_c=0
        for i in range(1,len(s)):
            if s[i-1]==s[i]-1:
                count+=1
                max_c=max(count,max_c)
            elif s[i-1]==s[i]:
                count
            else:
                count=0

        return max_c+1
        