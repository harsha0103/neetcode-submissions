class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        final=0
        for s in stones:
            final=abs(final-s)
        
        return final