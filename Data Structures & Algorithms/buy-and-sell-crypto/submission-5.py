class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tot_prof = 0

        l = 0 
        r = l + 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            curr_prof = prices[r] - prices[l]
            tot_prof = max(curr_prof, tot_prof)
            r+=1
        return tot_prof
