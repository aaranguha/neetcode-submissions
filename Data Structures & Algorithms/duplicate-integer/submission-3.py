class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = {}
        for i, v in enumerate(nums):
            if v in store:
                return True
            store[v] = i
        return False