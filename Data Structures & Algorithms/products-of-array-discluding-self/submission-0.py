class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [nums[0]]
        for i in range(1,len(nums)):
            forward.append(forward[i-1]*nums[i])

        backward = nums
        for i in range(2,len(nums)+1):
            backward[-i]*= backward[-i+1]

        backward = [1]+backward+[1]
        forward = [1]+forward+[1]

        out = []
        for i in range(1,len(nums)+1):
            out.append(forward[i-1]*backward[i+1])
        return out
            