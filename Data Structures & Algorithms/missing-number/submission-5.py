class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        true = sum(nums)
        return sum(num for num in range(len(nums)+1))-true