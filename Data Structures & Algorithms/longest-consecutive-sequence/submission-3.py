class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            print("empty")
            return 0
        soorted = sorted(set(nums))
        print(soorted)
        longest = 1
        prev = nums[0]
        temp = 1
        for num in soorted:
            if num == prev+1:
                temp+=1
                longest = max(longest, temp)
            else:
                temp = 1
            prev = num
            

        return longest