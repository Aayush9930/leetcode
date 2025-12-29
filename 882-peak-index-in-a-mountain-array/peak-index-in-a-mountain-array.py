class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l + r) // 2 

            if mid + 1 < len(arr) and arr[mid] < arr[mid + 1]:
                l = mid + 1
            
            elif  mid - 1 >= 0 and arr[mid - 1] > arr[mid]:
                r = mid - 1
            
            else:
                return mid