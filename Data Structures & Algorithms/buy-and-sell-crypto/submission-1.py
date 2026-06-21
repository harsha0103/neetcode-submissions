class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        max_profit=0
        for r in prices[1:]:
            if r-prices[l]<=0:
                l+=1
                continue
            else:
                max_profit=max(max_profit,r-prices[l])
        return max_profit