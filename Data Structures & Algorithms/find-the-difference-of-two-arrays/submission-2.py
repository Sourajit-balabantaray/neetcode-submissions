class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l=set(nums1)
        m=set(nums2)
        return [list(l-m),list(m-l)]
        