class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x, y = m - 1, n - 1
        i = len(nums1) - 1

        while y >= 0 and x >= 0:
            if nums1[x] <= nums2[y]:
                nums1[i] = nums2[y]
                y -= 1
                i -= 1
            
            elif nums1[x] > nums2[y]:
                temp = nums1[x]
                nums1[x] = 0
                nums1[i] = temp
                i -= 1
                x -= 1
        
        if y >= 0:
            while y >= 0:
                nums1[i] = nums2[y]
                i -= 1
                y -= 1
