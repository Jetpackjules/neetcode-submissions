class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # plan:
        # SORT! nlogn
        nums.sort()
        out = set()
        
        for i in range(len(nums)):
            target = -nums[i]
            
            bottom = i+1
            front = len(nums)-1
            while bottom < front:
                if target == nums[bottom] + nums[front]:
                    out.add((nums[i],nums[bottom],nums[front]))
                    front -= 1
                elif nums[bottom] + nums[front] < target:
                    bottom +=1
                else:
                    front -= 1
            i += 1
            
        
        return [list(trip) for trip in out]