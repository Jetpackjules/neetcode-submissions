class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for idx, num in enumerate(nums):
            diff = target-num
            if diff in pairs:
                return [pairs[diff], idx]
            pairs[num] = idx