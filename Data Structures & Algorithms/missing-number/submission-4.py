class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = set(nums)
        for num in range(len(nums)+1):
            if num not in expected:
                return num
        