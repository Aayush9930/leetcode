class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1          # last valid element in nums1
        j = n - 1          # last element in nums2
        k = m + n - 1      # last position in nums1 (full size)

        # Fill nums1 from the back
        while j >= 0:
            # If nums1 still has elements and its current is bigger, place it
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1