class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        vol = 0
        while left < right:
            lH = heights[left]
            rH = heights[right]

            tempVol = min(lH,rH)*(right-left)
            vol = max(vol, tempVol)
            # print(lH,rH, tempVol, vol, min(lH,rH), right, left)

            if lH < rH:
                left +=1
            else:
                right -=1
        return vol
