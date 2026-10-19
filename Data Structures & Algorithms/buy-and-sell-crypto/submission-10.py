class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tot_prof = 0
        l = 0
        r = 1

        while r <= len(prices) - 1:
            if prices[r] < prices[l]:
                l = r
            curr = prices[r] - prices[l]
            tot_prof = max(tot_prof, curr)
            r+=1
        return tot_prof