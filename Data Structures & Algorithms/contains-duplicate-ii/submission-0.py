class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set ()
        k +=1

        l=0
        for r in range(len(nums)):
            if r-l+1>k:
                window.remove(k)
                l+=1
            
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False
        