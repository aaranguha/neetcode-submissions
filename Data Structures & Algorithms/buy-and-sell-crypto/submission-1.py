class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tot_prof =  0
        l = 0
        r = 1
        while(r < len(prices)):
            if (prices[r] < prices[l]):
                l = r
            else:
                prof = prices[r] - prices[l]
                tot_prof = max(tot_prof, prof)
            r = r + 1
        return tot_prof