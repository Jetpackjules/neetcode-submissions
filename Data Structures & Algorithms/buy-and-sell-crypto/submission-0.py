class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Approach:
        #  iterate througb list
        #  track current best price so far,
        #  buy price (so we reset when it hits the same again?)

        #  edge cases:
        # empty list?
        #  only decreacing?
        #  same numebr?
        if not prices:
            return 0

        best = 0
        curr = prices[0]
        for price in prices:
            if price < curr:
                curr = price
            else:
                best = max(best, price-curr)


        return best
        