class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j=0,1
        res=0

        while j<len(prices)-1:
            total=prices[j]-prices[i]
            if total<=0:
                i+=1
                j+=1
            else:
                j+=1
                res=max(res,total)
        return res