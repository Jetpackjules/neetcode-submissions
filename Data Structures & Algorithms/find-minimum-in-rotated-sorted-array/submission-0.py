class Solution:
    def findMin(self, nums: List[int]) -> int:
        # what we are looking for i-1 > i!
        arr = nums
        while len(arr) > 1:
            half = (len(arr) - 1) // 2
            # print(arr)
            if arr[half] > arr[-1]:
                # print(arr[0], arr[half], "SEC")
                arr = arr[half+1:]  
            else:
                # print(arr[0], arr[half], "DIFF")
                arr = arr[:half+1]   
                
            # print(arr)
        return arr[0]


        