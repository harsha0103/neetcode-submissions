class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        max_r=float('-inf')
        for r in range(len(prices )):
            if prices[l]>prices[r]:
                l=r

            max_r=max(max_r,prices[r]-prices[l])
        return max_r