class Solution:
    def climbStairs(self, n: int) -> int:

        #DP: So, we:
        # 1: know the combos t get to the prev step,
        # 2: add the variations that the current step adds?
        # 3: move forward?
        # 
        # Edge cases:
        #  empty,
        #  0 steps
        if n < 3:
            return n

        tots = [1, 2]
        for i in range(2,n):
            tots.append(tots[-1] + tots[-2])
            

        return tots[-1]
