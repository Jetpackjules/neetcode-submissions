class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Onyl reason wed change lowest is ifits lower than prev lowerst? that woudl reset highest tho, but offer higher return.

        #  sliding window
        #  keep gowing till u hit a smaller small, then compare to higherst and move on



        # Edge cases:
        # None: return 0 (default)
        # all same: return 0
        # empty: return 0.

        prof = 0

        i = j = 0

        while j < len(prices):
            # update max profit
            if prices[j] < prices[i]:
                i = j
            prof = max(prof, prices[j] - prices[i])
            j+=1

        return prof
        