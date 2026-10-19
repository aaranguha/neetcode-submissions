class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        length = 0
        for i in nums_set:
            if (i-1) not in nums_set:
                curr = 1
                while(i + curr) in nums_set:
                    curr+=1
                length = max(length, curr)
        return length