class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        curr = 0
        for num in nums:
            if num != curr:
                return curr
            curr += 1
        return curr
        