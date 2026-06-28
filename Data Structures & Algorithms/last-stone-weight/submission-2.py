class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        final=0
        stones.sort()
        stones.reverse()
        for s in stones:
            final=abs(final-s)
        
        return final