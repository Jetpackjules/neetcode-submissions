class Solution:
    def rob(self, nums: List[int]) -> int:

        # dp

        # HOUSES [1, 3, 5, 6]
        # 1, rob 1
        # 2, rob 3
        # 3, rob 1 and 5
        # 4, rob 2 and 6
        # CHOICE: best of robbed last, OR best of  robbedbefore last!

        soFar = [0,0]

        for house in nums:
            soFar = [max(soFar[0], soFar[1]), soFar[0]+house]
            # print(soFar, house)

        return max(soFar)
        