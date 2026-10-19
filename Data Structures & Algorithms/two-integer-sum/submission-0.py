class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i,j in enumerate(nums):
            missing = target - j
            if missing in store:
                return (store[missing], i)
            else:
                store[j] = i
