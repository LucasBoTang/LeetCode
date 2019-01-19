class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        m, n = len(nums1), len(nums2)

        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        start, end = 0, m
        half = (m + n + 1) // 2
        odd = (m + n) % 2

        while start <= end:
            i = (start + end) // 2
            j = half - i
            # left > right
            if i > 0 and nums1[i-1] > nums2[j]:
                end = i - 1
            # left < right
            elif i < m and nums1[i] < nums2[j-1]:
                start = i + 1

            # pefect split
            else:
                if i == 0:
                    leftmax = nums2[j-1]
                elif j == 0:
                    leftmax = nums1[i-1]
                else:
                    leftmax = max(nums1[i-1], nums2[j-1])

                if odd:
                    return leftmax
                else:
                    if j == n:
                        rightmin = nums1[i]
                    elif i == m:
                        rightmin = nums2[j]
                    else:
                        rightmin = min(nums1[i], nums2[j])
                    return (leftmax + rightmin) / 2
