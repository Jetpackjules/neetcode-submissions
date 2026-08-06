class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        tots = [1, 2]
        for i in range(2,n):
            tots.append(tots[-1] + tots[-2])
            
        return tots[-1]
