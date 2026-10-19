class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i,v in enumerate(nums):
            answer = target - v
            if answer in store:
                return[store[answer], i]
            else:
                store[v] = i