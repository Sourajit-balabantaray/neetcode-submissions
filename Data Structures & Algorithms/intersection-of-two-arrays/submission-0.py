class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen=set(nums2)
        l=set()
        for i in nums1:
            if i in seen:
                l.add(i)
        return list(l)
        