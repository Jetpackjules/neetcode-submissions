class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for num in nums:
            freqs[num] = freqs.get(num, 0)+1

        return sorted(freqs.keys(), key = lambda x : freqs[x])[-k:]

        