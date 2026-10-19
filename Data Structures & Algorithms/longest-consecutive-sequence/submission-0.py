class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_sequence = 0
        for n in nums_set:
            if (n - 1) not in nums_set:
                length = 0
                while (n + length) in nums_set:
                    length+=1
                longest_sequence = max(longest_sequence, length)
        return longest_sequence