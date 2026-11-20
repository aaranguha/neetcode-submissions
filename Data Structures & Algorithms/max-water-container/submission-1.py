class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        total = 0

        while l < r:
            curr_total = (r - l) * min(heights[r], heights[l])
            total = max(total, curr_total)

            if heights[l] < heights[r]:
                l = l+1
            else:
                r = r - 1

        return total




    