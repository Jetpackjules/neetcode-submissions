class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}

        for idx, num in enumerate(nums):
            if num in pairs:
                return [pairs[num], idx]
            else:
                pairs[target-num] = idx

        # safe fail case
        return []