class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            store[nums[i]] = i
        for i in range (len(nums)):
            diff = target - nums[i]
            if diff in store and store[diff] != i:
                return [i, store[diff]]
        return []

                


        