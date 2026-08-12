class Solution:
    def rob(self, nums: List[int]) -> int:
        #  DP: two most recent houses, can only rob one! 
        # rob, not rob, not rob, rob
        # two states: if I DID, and DIDNT rob the alst house!
        # [did not rob, did rob] -> 
        # edge: empty,. or one house

        if not nums:
            return 0

        last2 = [0,0]

        for house in nums:
            last2 = [last2[1], max(last2[1], last2[0]+house)]
        
        return max(last2)
