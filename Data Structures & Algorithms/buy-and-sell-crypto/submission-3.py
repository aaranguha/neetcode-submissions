class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tot_prof = 0
        l = 0
        r = l + 1

        while (r < len(prices)):
            if prices[l] > prices[r]:
                l = r
            curr_prof = prices[r] - prices[l]
            tot_prof = max(tot_prof, curr_prof)
            r+=1
        return tot_prof
            