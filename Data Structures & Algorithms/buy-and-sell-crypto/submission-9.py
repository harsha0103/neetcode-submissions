class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j=0,1
        res=0

        while j<len(prices):
            total=prices[j]-prices[i]
            if total<=0:
                i=j
                j+=1
            else:
                j+=1
                res=max(res,total)
        return res