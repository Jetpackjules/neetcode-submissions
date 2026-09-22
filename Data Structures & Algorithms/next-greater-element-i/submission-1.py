class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Iterate left to right.
        # if a new num is bigger than top f hash, pop until from hash until it is smaller, and save to a dict, and if a nums1 number was popped, savethat one as its next greatest!


        pos = {num: i for i, num in enumerate(nums1)}
        out = [-1]*len(nums1)

        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                smol = stack.pop()
                if smol in pos:
                    out[pos[smol]] = num
            stack.append(num)

        return out
