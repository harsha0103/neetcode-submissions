class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        max_profit=0
        for r in range(1,len(prices[1:])):
            if prices[l]>=prices[r]:
                l=r
                continue
            else:
                max_profit=max(max_profit,prices[r]-prices[l])
        return max_profit