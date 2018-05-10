class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = [-1] * len(nums1)
        for i in range(len(nums1)):
            j = nums2.index(nums1[i]) + 1
            while j < len(nums2):
                if nums1[i] < nums2[j]:
                    result[i] = nums2[j]
                    break
                j += 1
        return result
