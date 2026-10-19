class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = {}
        for i,j in enumerate(nums):
            if j in store:
                return True
            else:
                store[j] = i
        return False
