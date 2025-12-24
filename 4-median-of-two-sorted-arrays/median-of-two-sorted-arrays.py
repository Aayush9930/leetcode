class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        total = len(nums1) + len(nums2)
        half = (total + 1) // 2

        l, r = 0, len(nums1)

        while l <= r:
            mid1 = (l + r) // 2
            mid2 = half - mid1

            l1 = nums1[mid1 - 1] if mid1 - 1 >= 0 else float('-inf')
            l2 = nums2[mid2 - 1] if mid2 - 1 >= 0 else float('-inf')
            r1 = nums1[mid1] if mid1 < len(nums1) else float('inf')
            r2 = nums2[mid2] if mid2 < len(nums2) else float('inf')
        
            if l1 > r2:
                r = mid1 - 1
            
            elif l2 > r1:
                l = mid1 + 1
            
            else:
                if total % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)
        



