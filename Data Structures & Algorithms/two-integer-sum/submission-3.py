class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i,v in enumerate(nums):
            missing = target - v
            if missing in store:
                return[store[missing], i]
            else:
                store[v] = i